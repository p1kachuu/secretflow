import os
import tempfile
from dataclasses import dataclass

import numpy as np
import pytest
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

import secretflow as sf
import secretflow.distributed as sfd
from secretflow.device import global_state
from secretflow.device.device.teeu import TEEU
from secretflow.utils.testing import unused_tcp_port
from tests.cluster import cluster, get_self_party, set_self_party
from tests.utils.auth_manager import start_auth_server


@dataclass
class TeeuTestInventory:
    alice: sf.PYU = None
    bob: sf.PYU = None
    carol: sf.PYU = None
    davy: sf.PYU = None
    tmp_files: list = None


@pytest.fixture(scope="module")
def teeu_production_setup_devices(request, sf_party_for_4pc):
    inventory = TeeuTestInventory()
    sfd.set_production(True)
    set_self_party(sf_party_for_4pc)
    self_party = get_self_party()
    if self_party in ('carol', 'davy'):
        sf.init(
            address='local',
            cluster_config=cluster(),
            logging_level='debug',
            num_cpus=8,
            log_to_driver=True,
            tee_simulation=True,
            enable_waiting_for_other_parties_ready=False,
        )

    elif self_party in ('alice', 'bob'):
        _, private_key_path = tempfile.mkstemp()
        _, public_key_path = tempfile.mkstemp()
        inventory.tmp_files = [private_key_path, public_key_path]

        def gen_rsa(pub_path: str, pri_path: str):
            key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
            key_contents = key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption(),
            )
            public_key = key.public_key().public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo,
            )
            with open(pri_path, 'wb') as f:
                f.write(key_contents)
            with open(pub_path, 'wb') as f:
                f.write(public_key)

        gen_rsa(public_key_path, private_key_path)

        if self_party == 'alice':
            party_key_pair = {
                'alice': {
                    'public_key': public_key_path,
                    'private_key': private_key_path,
                },
            }
        else:
            party_key_pair = {
                'bob': {
                    'public_key': public_key_path,
                    'private_key': private_key_path,
                },
            }
        sf.init(
            address='local',
            cluster_config=cluster(),
            num_cpus=8,
            log_to_driver=True,
            party_key_pair=party_key_pair,
            tee_simulation=True,
            enable_waiting_for_other_parties_ready=False,
        )

    inventory.alice = sf.PYU('alice')
    inventory.bob = sf.PYU('bob')
    inventory.carol = sf.PYU('carol')
    inventory.davy = sf.PYU('davy')

    auth_port = sf.reveal(inventory.carol(unused_tcp_port)())
    global_state.set_auth_manager_host(f'127.0.0.1:{auth_port}')

    if self_party == 'carol':
        inventory.server = start_auth_server(auth_port)

    yield inventory

    if inventory.tmp_files:
        for file in inventory.tmp_files:
            try:
                os.remove(file)
            except SystemError:
                # Do nothing.
                pass
    del inventory
    sf.shutdown()


def test(teeu_production_setup_devices):
    def average(data):
        return np.average(data, axis=0)

    teeu = TEEU(party='carol', mr_enclave='')
    d1 = teeu_production_setup_devices.alice(lambda: np.random.random([2, 4]))()
    d2 = teeu_production_setup_devices.bob(lambda: np.random.random([2, 4]))()
    d1_tee = d1.to(teeu, allow_funcs=average)
    d2_tee = d2.to(teeu, allow_funcs=average)
    avg_val = teeu(average)([d1_tee, d2_tee])
    avg_val = sf.reveal(avg_val)
    expected_avg = average(sf.reveal([d1, d2]))
    np.testing.assert_equal(avg_val, expected_avg)