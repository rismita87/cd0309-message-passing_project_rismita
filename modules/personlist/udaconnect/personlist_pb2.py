# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: personlist.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'personlist.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10personlist.proto\x12\x06person\"Q\n\x06Person\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x12\n\nfirst_name\x18\x02 \x01(\t\x12\x11\n\tlast_name\x18\x03 \x01(\t\x12\x14\n\x0c\x63ompany_name\x18\x04 \x01(\t\",\n\nPersonList\x12\x1e\n\x06people\x18\x01 \x03(\x0b\x32\x0e.person.Person\"\x0e\n\x0c\x45mptyRequest2J\n\rPersonService\x12\x39\n\rGetAllPersons\x12\x14.person.EmptyRequest\x1a\x12.person.PersonListb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'personlist_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_PERSON']._serialized_start=28
  _globals['_PERSON']._serialized_end=109
  _globals['_PERSONLIST']._serialized_start=111
  _globals['_PERSONLIST']._serialized_end=155
  _globals['_EMPTYREQUEST']._serialized_start=157
  _globals['_EMPTYREQUEST']._serialized_end=171
  _globals['_PERSONSERVICE']._serialized_start=173
  _globals['_PERSONSERVICE']._serialized_end=247
# @@protoc_insertion_point(module_scope)
