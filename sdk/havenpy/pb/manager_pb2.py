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




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rmanager.proto\x12\x05haven\"\x07\n\x05\x45mpty\"^\n\x0cSetupRequest\x12\x15\n\x08key_file\x18\x01 \x01(\tH\x00\x88\x01\x01\x12 \n\x05\x63loud\x18\x02 \x01(\x0e\x32\x0c.haven.CloudH\x01\x88\x01\x01\x42\x0b\n\t_key_fileB\x08\n\x06_cloud\";\n\x0b\x43loudStatus\x12\x1b\n\x05\x63loud\x18\x01 \x01(\x0e\x32\x0c.haven.Cloud\x12\x0f\n\x07\x65nabled\x18\x02 \x01(\x08\"[\n\rSetupResponse\x12\x14\n\x07message\x18\x01 \x01(\tH\x00\x88\x01\x01\x12(\n\x0c\x63loud_status\x18\x02 \x03(\x0b\x32\x12.haven.CloudStatusB\n\n\x08_message\"5\n\x07Message\x12\x19\n\x04role\x18\x01 \x01(\x0e\x32\x0b.haven.Role\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\"\xdc\x01\n\x15\x43hatCompletionRequest\x12\x13\n\x0bworker_name\x18\x01 \x01(\t\x12 \n\x08messages\x18\x02 \x03(\x0b\x32\x0e.haven.Message\x12\x17\n\nmax_tokens\x18\x03 \x01(\x05H\x00\x88\x01\x01\x12\x12\n\x05top_p\x18\x04 \x01(\x02H\x01\x88\x01\x01\x12\x12\n\x05top_k\x18\x05 \x01(\x05H\x02\x88\x01\x01\x12\x18\n\x0btemperature\x18\x06 \x01(\x02H\x03\x88\x01\x01\x42\r\n\x0b_max_tokensB\x08\n\x06_top_pB\x08\n\x06_top_kB\x0e\n\x0c_temperature\"\xdb\x01\n\x11\x43ompletionRequest\x12\x13\n\x0bworker_name\x18\x01 \x01(\t\x12\x0e\n\x06prompt\x18\x02 \x01(\t\x12\x13\n\x0bstop_tokens\x18\x07 \x03(\t\x12\x17\n\nmax_tokens\x18\x03 \x01(\x05H\x00\x88\x01\x01\x12\x12\n\x05top_p\x18\x04 \x01(\x02H\x01\x88\x01\x01\x12\x12\n\x05top_k\x18\x05 \x01(\x05H\x02\x88\x01\x01\x12\x18\n\x0btemperature\x18\x06 \x01(\x02H\x03\x88\x01\x01\x42\r\n\x0b_max_tokensB\x08\n\x06_top_pB\x08\n\x06_top_kB\x0e\n\x0c_temperature\"\"\n\x12\x43ompletionResponse\x12\x0c\n\x04text\x18\x01 \x01(\t\"\xbc\x02\n\x05Model\x12\x14\n\x0c\x61rchitecture\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\ttokenizer\x18\x03 \x01(\t\x12\x1a\n\rsystem_prompt\x18\x04 \x01(\tH\x00\x88\x01\x01\x12\x1f\n\x12instruction_prefix\x18\x05 \x01(\tH\x01\x88\x01\x01\x12 \n\x13instruction_postfix\x18\x06 \x01(\tH\x02\x88\x01\x01\x12\x1a\n\routput_prefix\x18\x07 \x01(\tH\x03\x88\x01\x01\x12\x1b\n\x0eoutput_postfix\x18\x08 \x01(\tH\x04\x88\x01\x01\x42\x10\n\x0e_system_promptB\x15\n\x13_instruction_prefixB\x16\n\x14_instruction_postfixB\x10\n\x0e_output_prefixB\x11\n\x0f_output_postfix\"\x19\n\tModelName\x12\x0c\n\x04name\x18\x01 \x01(\t\"2\n\x12ListModelsResponse\x12\x1c\n\x06models\x18\x01 \x03(\x0b\x32\x0c.haven.Model\"Y\n\x06Worker\x12\x13\n\x0bworker_name\x18\x01 \x01(\t\x12\x1d\n\x06status\x18\x02 \x01(\x0e\x32\r.haven.Status\x12\x1b\n\x05\x63loud\x18\x03 \x01(\x0e\x32\x0c.haven.Cloud\"5\n\x13ListWorkersResponse\x12\x1e\n\x07workers\x18\x01 \x03(\x0b\x32\r.haven.Worker\"\x94\x02\n\x1c\x43reateInferenceWorkerRequest\x12\x12\n\nmodel_name\x18\x01 \x01(\t\x12\x14\n\x0cquantization\x18\x02 \x01(\t\x12\x18\n\x0bworker_name\x18\x03 \x01(\tH\x00\x88\x01\x01\x12 \n\x05\x63loud\x18\x08 \x01(\x0e\x32\x0c.haven.CloudH\x01\x88\x01\x01\x12%\n\x08gpu_type\x18\x04 \x01(\x0e\x32\x0e.haven.GpuTypeH\x02\x88\x01\x01\x12\x16\n\tgpu_count\x18\x06 \x01(\x05H\x03\x88\x01\x01\x12\x11\n\x04zone\x18\x07 \x01(\tH\x04\x88\x01\x01\x42\x0e\n\x0c_worker_nameB\x08\n\x06_cloudB\x0b\n\t_gpu_typeB\x0c\n\n_gpu_countB\x07\n\x05_zone\"&\n\x0fInferenceWorker\x12\x13\n\x0bworker_name\x18\x01 \x01(\t*\x19\n\x05\x43loud\x12\x07\n\x03GCP\x10\x00\x12\x07\n\x03\x41WS\x10\x01*\x1f\n\x04Role\x12\r\n\tASSISTANT\x10\x00\x12\x08\n\x04USER\x10\x01*8\n\x06Status\x12\n\n\x06ONLINE\x10\x00\x12\x0b\n\x07LOADING\x10\x01\x12\n\n\x06PAUSED\x10\x02\x12\t\n\x05\x45RROR\x10\x03**\n\x07GpuType\x12\x08\n\x04\x41\x31\x30\x30\x10\x00\x12\r\n\tA100_80GB\x10\x01\x12\x06\n\x02T4\x10\x02\x32\xda\x05\n\x05Haven\x12\x34\n\x05Setup\x12\x13.haven.SetupRequest\x1a\x14.haven.SetupResponse\"\x00\x12M\n\x0e\x43hatCompletion\x12\x1c.haven.ChatCompletionRequest\x1a\x19.haven.CompletionResponse\"\x00\x30\x01\x12\x45\n\nCompletion\x12\x18.haven.CompletionRequest\x1a\x19.haven.CompletionResponse\"\x00\x30\x01\x12\x37\n\nListModels\x12\x0c.haven.Empty\x1a\x19.haven.ListModelsResponse\"\x00\x12(\n\x08\x41\x64\x64Model\x12\x0c.haven.Model\x1a\x0c.haven.Empty\"\x00\x12/\n\x0b\x44\x65leteModel\x12\x10.haven.ModelName\x1a\x0c.haven.Empty\"\x00\x12\x39\n\x0bListWorkers\x12\x0c.haven.Empty\x1a\x1a.haven.ListWorkersResponse\"\x00\x12V\n\x15\x43reateInferenceWorker\x12#.haven.CreateInferenceWorkerRequest\x1a\x16.haven.InferenceWorker\"\x00\x12H\n\x14PauseInferenceWorker\x12\x16.haven.InferenceWorker\x1a\x16.haven.InferenceWorker\"\x00\x12I\n\x15ResumeInferenceWorker\x12\x16.haven.InferenceWorker\x1a\x16.haven.InferenceWorker\"\x00\x12I\n\x15\x44\x65leteInferenceWorker\x12\x16.haven.InferenceWorker\x1a\x16.haven.InferenceWorker\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'manager_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CLOUD._serialized_start=1682
  _CLOUD._serialized_end=1707
  _ROLE._serialized_start=1709
  _ROLE._serialized_end=1740
  _STATUS._serialized_start=1742
  _STATUS._serialized_end=1798
  _GPUTYPE._serialized_start=1800
  _GPUTYPE._serialized_end=1842
  _EMPTY._serialized_start=24
  _EMPTY._serialized_end=31
  _SETUPREQUEST._serialized_start=33
  _SETUPREQUEST._serialized_end=127
  _CLOUDSTATUS._serialized_start=129
  _CLOUDSTATUS._serialized_end=188
  _SETUPRESPONSE._serialized_start=190
  _SETUPRESPONSE._serialized_end=281
  _MESSAGE._serialized_start=283
  _MESSAGE._serialized_end=336
  _CHATCOMPLETIONREQUEST._serialized_start=339
  _CHATCOMPLETIONREQUEST._serialized_end=559
  _COMPLETIONREQUEST._serialized_start=562
  _COMPLETIONREQUEST._serialized_end=781
  _COMPLETIONRESPONSE._serialized_start=783
  _COMPLETIONRESPONSE._serialized_end=817
  _MODEL._serialized_start=820
  _MODEL._serialized_end=1136
  _MODELNAME._serialized_start=1138
  _MODELNAME._serialized_end=1163
  _LISTMODELSRESPONSE._serialized_start=1165
  _LISTMODELSRESPONSE._serialized_end=1215
  _WORKER._serialized_start=1217
  _WORKER._serialized_end=1306
  _LISTWORKERSRESPONSE._serialized_start=1308
  _LISTWORKERSRESPONSE._serialized_end=1361
  _CREATEINFERENCEWORKERREQUEST._serialized_start=1364
  _CREATEINFERENCEWORKERREQUEST._serialized_end=1640
  _INFERENCEWORKER._serialized_start=1642
  _INFERENCEWORKER._serialized_end=1680
  _HAVEN._serialized_start=1845
  _HAVEN._serialized_end=2575
# @@protoc_insertion_point(module_scope)
