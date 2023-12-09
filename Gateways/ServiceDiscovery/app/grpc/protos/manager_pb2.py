# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: manager.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rmanager.proto\x12\x07manager\"\x18\n\x16GetHealthStatusRequest\"t\n\x17GetHealthStatusResponse\x12+\n\x0chealthStatus\x18\x01 \x01(\x0e\x32\x15.manager.HealthStatus\x12\x1a\n\rstatusMessage\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x10\n\x0e_statusMessage\"Q\n\x16RegisterServiceRequest\x12)\n\x0bserviceType\x18\x01 \x01(\x0e\x32\x14.manager.ServiceType\x12\x0c\n\x04host\x18\x02 \x01(\t\"\x19\n\x17RegisterServiceResponse\"B\n\x15GetServiceHostRequest\x12)\n\x0bserviceType\x18\x01 \x01(\x0e\x32\x14.manager.ServiceType\"&\n\x16GetServiceHostResponse\x12\x0c\n\x04host\x18\x01 \x01(\t* \n\x0cHealthStatus\x12\x06\n\x02Up\x10\x00\x12\x08\n\x04\x44own\x10\x01*+\n\x0bServiceType\x12\x0b\n\x07\x41\x63\x63ount\x10\x00\x12\x0f\n\x0bTransaction\x10\x01\x32\x8f\x02\n\x0eManagerService\x12T\n\x0fGetHealthStatus\x12\x1f.manager.GetHealthStatusRequest\x1a .manager.GetHealthStatusResponse\x12T\n\x0fRegisterService\x12\x1f.manager.RegisterServiceRequest\x1a .manager.RegisterServiceResponse\x12Q\n\x0eGetServiceHost\x12\x1e.manager.GetServiceHostRequest\x1a\x1f.manager.GetServiceHostResponseB\x11\xaa\x02\x0eProtos.Managerb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'manager_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002\016Protos.Manager'
  _globals['_HEALTHSTATUS']._serialized_start=388
  _globals['_HEALTHSTATUS']._serialized_end=420
  _globals['_SERVICETYPE']._serialized_start=422
  _globals['_SERVICETYPE']._serialized_end=465
  _globals['_GETHEALTHSTATUSREQUEST']._serialized_start=26
  _globals['_GETHEALTHSTATUSREQUEST']._serialized_end=50
  _globals['_GETHEALTHSTATUSRESPONSE']._serialized_start=52
  _globals['_GETHEALTHSTATUSRESPONSE']._serialized_end=168
  _globals['_REGISTERSERVICEREQUEST']._serialized_start=170
  _globals['_REGISTERSERVICEREQUEST']._serialized_end=251
  _globals['_REGISTERSERVICERESPONSE']._serialized_start=253
  _globals['_REGISTERSERVICERESPONSE']._serialized_end=278
  _globals['_GETSERVICEHOSTREQUEST']._serialized_start=280
  _globals['_GETSERVICEHOSTREQUEST']._serialized_end=346
  _globals['_GETSERVICEHOSTRESPONSE']._serialized_start=348
  _globals['_GETSERVICEHOSTRESPONSE']._serialized_end=386
  _globals['_MANAGERSERVICE']._serialized_start=468
  _globals['_MANAGERSERVICE']._serialized_end=739
# @@protoc_insertion_point(module_scope)
