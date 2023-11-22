# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: phe.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tphe.proto\x12\x1forg.interconnection.v2.protocol\x1a\x19google/protobuf/any.proto\"\x82\x01\n\x13PheProtocolProposal\x12\x1a\n\x12supported_versions\x18\x01 \x03(\x05\x12\x1b\n\x13supported_phe_algos\x18\x02 \x03(\x05\x12\x32\n\x14supported_phe_params\x18\x03 \x03(\x0b\x32\x14.google.protobuf.Any\"+\n\x16PaillierParamsProposal\x12\x11\n\tkey_sizes\x18\x01 \x03(\x05\"_\n\x11PheProtocolResult\x12\x0f\n\x07version\x18\x01 \x01(\x05\x12\x10\n\x08phe_algo\x18\x02 \x01(\x05\x12\'\n\tphe_param\x18\x03 \x01(\x0b\x32\x14.google.protobuf.Any\"(\n\x14PaillierParamsResult\x12\x10\n\x08key_size\x18\x01 \x01(\x05*d\n\x07PheAlgo\x12\x18\n\x14PHE_ALGO_UNSPECIFIED\x10\x00\x12\x15\n\x11PHE_ALGO_PAILLIER\x10\x01\x12\x0f\n\x0bPHE_ALGO_OU\x10\x02\x12\x17\n\x13PHE_ALGO_EC_ELGAMAL\x10\x03\x62\x06proto3')

_PHEALGO = DESCRIPTOR.enum_types_by_name['PheAlgo']
PheAlgo = enum_type_wrapper.EnumTypeWrapper(_PHEALGO)
PHE_ALGO_UNSPECIFIED = 0
PHE_ALGO_PAILLIER = 1
PHE_ALGO_OU = 2
PHE_ALGO_EC_ELGAMAL = 3


_PHEPROTOCOLPROPOSAL = DESCRIPTOR.message_types_by_name['PheProtocolProposal']
_PAILLIERPARAMSPROPOSAL = DESCRIPTOR.message_types_by_name['PaillierParamsProposal']
_PHEPROTOCOLRESULT = DESCRIPTOR.message_types_by_name['PheProtocolResult']
_PAILLIERPARAMSRESULT = DESCRIPTOR.message_types_by_name['PaillierParamsResult']
PheProtocolProposal = _reflection.GeneratedProtocolMessageType('PheProtocolProposal', (_message.Message,), {
  'DESCRIPTOR' : _PHEPROTOCOLPROPOSAL,
  '__module__' : 'phe_pb2'
  # @@protoc_insertion_point(class_scope:org.interconnection.v2.protocol.PheProtocolProposal)
  })
_sym_db.RegisterMessage(PheProtocolProposal)

PaillierParamsProposal = _reflection.GeneratedProtocolMessageType('PaillierParamsProposal', (_message.Message,), {
  'DESCRIPTOR' : _PAILLIERPARAMSPROPOSAL,
  '__module__' : 'phe_pb2'
  # @@protoc_insertion_point(class_scope:org.interconnection.v2.protocol.PaillierParamsProposal)
  })
_sym_db.RegisterMessage(PaillierParamsProposal)

PheProtocolResult = _reflection.GeneratedProtocolMessageType('PheProtocolResult', (_message.Message,), {
  'DESCRIPTOR' : _PHEPROTOCOLRESULT,
  '__module__' : 'phe_pb2'
  # @@protoc_insertion_point(class_scope:org.interconnection.v2.protocol.PheProtocolResult)
  })
_sym_db.RegisterMessage(PheProtocolResult)

PaillierParamsResult = _reflection.GeneratedProtocolMessageType('PaillierParamsResult', (_message.Message,), {
  'DESCRIPTOR' : _PAILLIERPARAMSRESULT,
  '__module__' : 'phe_pb2'
  # @@protoc_insertion_point(class_scope:org.interconnection.v2.protocol.PaillierParamsResult)
  })
_sym_db.RegisterMessage(PaillierParamsResult)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PHEALGO._serialized_start=390
  _PHEALGO._serialized_end=490
  _PHEPROTOCOLPROPOSAL._serialized_start=74
  _PHEPROTOCOLPROPOSAL._serialized_end=204
  _PAILLIERPARAMSPROPOSAL._serialized_start=206
  _PAILLIERPARAMSPROPOSAL._serialized_end=249
  _PHEPROTOCOLRESULT._serialized_start=251
  _PHEPROTOCOLRESULT._serialized_end=346
  _PAILLIERPARAMSRESULT._serialized_start=348
  _PAILLIERPARAMSRESULT._serialized_end=388
# @@protoc_insertion_point(module_scope)