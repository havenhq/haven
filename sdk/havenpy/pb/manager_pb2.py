# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: manager.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rmanager.proto\x12\x05haven\"\x07\n\x05\x45mpty\"2\n\x0cSetupRequest\x12\x15\n\x08key_file\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\x0b\n\t_key_file\"1\n\rSetupResponse\x12\x14\n\x07message\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\n\n\x08_message\"5\n\x07Message\x12\x19\n\x04role\x18\x01 \x01(\x0e\x32\x0b.haven.Role\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\"\xdc\x01\n\x15\x43hatCompletionRequest\x12\x13\n\x0bworker_name\x18\x01 \x01(\t\x12 \n\x08messages\x18\x02 \x03(\x0b\x32\x0e.haven.Message\x12\x17\n\nmax_tokens\x18\x03 \x01(\x05H\x00\x88\x01\x01\x12\x12\n\x05top_p\x18\x04 \x01(\x02H\x01\x88\x01\x01\x12\x12\n\x05top_k\x18\x05 \x01(\x05H\x02\x88\x01\x01\x12\x18\n\x0btemperature\x18\x06 \x01(\x02H\x03\x88\x01\x01\x42\r\n\x0b_max_tokensB\x08\n\x06_top_pB\x08\n\x06_top_kB\x0e\n\x0c_temperature\"&\n\x16\x43hatCompletionResponse\x12\x0c\n\x04text\x18\x01 \x01(\t\"\x15\n\x05Model\x12\x0c\n\x04name\x18\x01 \x01(\t\"2\n\x12ListModelsResponse\x12\x1c\n\x06models\x18\x01 \x03(\x0b\x32\x0c.haven.Model\"<\n\x06Worker\x12\x13\n\x0bworker_name\x18\x01 \x01(\t\x12\x1d\n\x06status\x18\x02 \x01(\x0e\x32\r.haven.Status\"5\n\x13ListWorkersResponse\x12\x1e\n\x07workers\x18\x01 \x03(\x0b\x32\r.haven.Worker\"\xe8\x01\n\x1c\x43reateInferenceWorkerRequest\x12\x12\n\nmodel_name\x18\x01 \x01(\t\x12\x14\n\x0cquantization\x18\x02 \x01(\t\x12\x18\n\x0bworker_name\x18\x03 \x01(\tH\x00\x88\x01\x01\x12%\n\x08gpu_type\x18\x04 \x01(\x0e\x32\x0e.haven.GpuTypeH\x01\x88\x01\x01\x12\x16\n\tgpu_count\x18\x06 \x01(\x05H\x02\x88\x01\x01\x12\x11\n\x04zone\x18\x07 \x01(\tH\x03\x88\x01\x01\x42\x0e\n\x0c_worker_nameB\x0b\n\t_gpu_typeB\x0c\n\n_gpu_countB\x07\n\x05_zone\"&\n\x0fInferenceWorker\x12\x13\n\x0bworker_name\x18\x01 \x01(\t*\x1f\n\x04Role\x12\r\n\tASSISTANT\x10\x00\x12\x08\n\x04USER\x10\x01*<\n\x06Status\x12\n\n\x06ONLINE\x10\x00\x12\x0f\n\x0bUNREACHABLE\x10\x01\x12\n\n\x06PAUSED\x10\x02\x12\t\n\x05\x45RROR\x10\x03**\n\x07GpuType\x12\x08\n\x04\x41\x31\x30\x30\x10\x00\x12\r\n\tA100_80GB\x10\x01\x12\x06\n\x02T4\x10\x02\x32\xbc\x04\n\x05Haven\x12\x34\n\x05Setup\x12\x13.haven.SetupRequest\x1a\x14.haven.SetupResponse\"\x00\x12Q\n\x0e\x43hatCompletion\x12\x1c.haven.ChatCompletionRequest\x1a\x1d.haven.ChatCompletionResponse\"\x00\x30\x01\x12\x37\n\nListModels\x12\x0c.haven.Empty\x1a\x19.haven.ListModelsResponse\"\x00\x12\x39\n\x0bListWorkers\x12\x0c.haven.Empty\x1a\x1a.haven.ListWorkersResponse\"\x00\x12V\n\x15\x43reateInferenceWorker\x12#.haven.CreateInferenceWorkerRequest\x1a\x16.haven.InferenceWorker\"\x00\x12H\n\x14PauseInferenceWorker\x12\x16.haven.InferenceWorker\x1a\x16.haven.InferenceWorker\"\x00\x12I\n\x15ResumeInferenceWorker\x12\x16.haven.InferenceWorker\x1a\x16.haven.InferenceWorker\"\x00\x12I\n\x15\x44\x65leteInferenceWorker\x12\x16.haven.InferenceWorker\x1a\x16.haven.InferenceWorker\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'manager_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ROLE._serialized_start=921
  _ROLE._serialized_end=952
  _STATUS._serialized_start=954
  _STATUS._serialized_end=1014
  _GPUTYPE._serialized_start=1016
  _GPUTYPE._serialized_end=1058
  _EMPTY._serialized_start=24
  _EMPTY._serialized_end=31
  _SETUPREQUEST._serialized_start=33
  _SETUPREQUEST._serialized_end=83
  _SETUPRESPONSE._serialized_start=85
  _SETUPRESPONSE._serialized_end=134
  _MESSAGE._serialized_start=136
  _MESSAGE._serialized_end=189
  _CHATCOMPLETIONREQUEST._serialized_start=192
  _CHATCOMPLETIONREQUEST._serialized_end=412
  _CHATCOMPLETIONRESPONSE._serialized_start=414
  _CHATCOMPLETIONRESPONSE._serialized_end=452
  _MODEL._serialized_start=454
  _MODEL._serialized_end=475
  _LISTMODELSRESPONSE._serialized_start=477
  _LISTMODELSRESPONSE._serialized_end=527
  _WORKER._serialized_start=529
  _WORKER._serialized_end=589
  _LISTWORKERSRESPONSE._serialized_start=591
  _LISTWORKERSRESPONSE._serialized_end=644
  _CREATEINFERENCEWORKERREQUEST._serialized_start=647
  _CREATEINFERENCEWORKERREQUEST._serialized_end=879
  _INFERENCEWORKER._serialized_start=881
  _INFERENCEWORKER._serialized_end=919
  _HAVEN._serialized_start=1061
  _HAVEN._serialized_end=1633
# @@protoc_insertion_point(module_scope)
