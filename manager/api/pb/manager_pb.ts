// @generated by protoc-gen-es v1.2.1 with parameter "target=ts"
// @generated from file manager.proto (package haven, syntax proto3)
/* eslint-disable */
// @ts-nocheck

import type { BinaryReadOptions, FieldList, JsonReadOptions, JsonValue, PartialMessage, PlainMessage } from "@bufbuild/protobuf";
import { Message as Message$1, proto3 } from "@bufbuild/protobuf";

/**
 * @generated from enum haven.Role
 */
export enum Role {
  /**
   * @generated from enum value: ASSISTANT = 0;
   */
  ASSISTANT = 0,

  /**
   * @generated from enum value: USER = 1;
   */
  USER = 1,
}
// Retrieve enum metadata with: proto3.getEnumType(Role)
proto3.util.setEnumType(Role, "haven.Role", [
  { no: 0, name: "ASSISTANT" },
  { no: 1, name: "USER" },
]);

/**
 * @generated from enum haven.Status
 */
export enum Status {
  /**
   * @generated from enum value: ONLINE = 0;
   */
  ONLINE = 0,

  /**
   * @generated from enum value: UNREACHABLE = 1;
   */
  UNREACHABLE = 1,

  /**
   * @generated from enum value: PAUSED = 2;
   */
  PAUSED = 2,

  /**
   * @generated from enum value: ERROR = 3;
   */
  ERROR = 3,
}
// Retrieve enum metadata with: proto3.getEnumType(Status)
proto3.util.setEnumType(Status, "haven.Status", [
  { no: 0, name: "ONLINE" },
  { no: 1, name: "UNREACHABLE" },
  { no: 2, name: "PAUSED" },
  { no: 3, name: "ERROR" },
]);

/**
 * @generated from enum haven.GpuType
 */
export enum GpuType {
  /**
   * @generated from enum value: A100 = 0;
   */
  A100 = 0,

  /**
   * @generated from enum value: A100_80GB = 1;
   */
  A100_80GB = 1,

  /**
   * @generated from enum value: T4 = 2;
   */
  T4 = 2,
}
// Retrieve enum metadata with: proto3.getEnumType(GpuType)
proto3.util.setEnumType(GpuType, "haven.GpuType", [
  { no: 0, name: "A100" },
  { no: 1, name: "A100_80GB" },
  { no: 2, name: "T4" },
]);

/**
 * @generated from message haven.Empty
 */
export class Empty extends Message$1<Empty> {
  constructor(data?: PartialMessage<Empty>) {
    super();
    proto3.util.initPartial(data, this);
  }

  static readonly runtime: typeof proto3 = proto3;
  static readonly typeName = "haven.Empty";
  static readonly fields: FieldList = proto3.util.newFieldList(() => [
  ]);

  static fromBinary(bytes: Uint8Array, options?: Partial<BinaryReadOptions>): Empty {
    return new Empty().fromBinary(bytes, options);
  }

  static fromJson(jsonValue: JsonValue, options?: Partial<JsonReadOptions>): Empty {
    return new Empty().fromJson(jsonValue, options);
  }

  static fromJsonString(jsonString: string, options?: Partial<JsonReadOptions>): Empty {
    return new Empty().fromJsonString(jsonString, options);
  }

  static equals(a: Empty | PlainMessage<Empty> | undefined, b: Empty | PlainMessage<Empty> | undefined): boolean {
    return proto3.util.equals(Empty, a, b);
  }
}

/**
 * @generated from message haven.SetupRequest
 */
export class SetupRequest extends Message$1<SetupRequest> {
  /**
   * @generated from field: optional string key_file = 1;
   */
  keyFile?: string;

  constructor(data?: PartialMessage<SetupRequest>) {
    super();
    proto3.util.initPartial(data, this);
  }

  static readonly runtime: typeof proto3 = proto3;
  static readonly typeName = "haven.SetupRequest";
  static readonly fields: FieldList = proto3.util.newFieldList(() => [
    { no: 1, name: "key_file", kind: "scalar", T: 9 /* ScalarType.STRING */, opt: true },
  ]);

  static fromBinary(bytes: Uint8Array, options?: Partial<BinaryReadOptions>): SetupRequest {
    return new SetupRequest().fromBinary(bytes, options);
  }

  static fromJson(jsonValue: JsonValue, options?: Partial<JsonReadOptions>): SetupRequest {
    return new SetupRequest().fromJson(jsonValue, options);
  }

  static fromJsonString(jsonString: string, options?: Partial<JsonReadOptions>): SetupRequest {
    return new SetupRequest().fromJsonString(jsonString, options);
  }

  static equals(a: SetupRequest | PlainMessage<SetupRequest> | undefined, b: SetupRequest | PlainMessage<SetupRequest> | undefined): boolean {
    return proto3.util.equals(SetupRequest, a, b);
  }
}

/**
 * @generated from message haven.SetupResponse
 */
export class SetupResponse extends Message$1<SetupResponse> {
  /**
   * Used for warnings when running on an outdated version.
   *
   * @generated from field: optional string message = 1;
   */
  message?: string;

  constructor(data?: PartialMessage<SetupResponse>) {
    super();
    proto3.util.initPartial(data, this);
  }

  static readonly runtime: typeof proto3 = proto3;
  static readonly typeName = "haven.SetupResponse";
  static readonly fields: FieldList = proto3.util.newFieldList(() => [
    { no: 1, name: "message", kind: "scalar", T: 9 /* ScalarType.STRING */, opt: true },
  ]);

  static fromBinary(bytes: Uint8Array, options?: Partial<BinaryReadOptions>): SetupResponse {
    return new SetupResponse().fromBinary(bytes, options);
  }

  static fromJson(jsonValue: JsonValue, options?: Partial<JsonReadOptions>): SetupResponse {
    return new SetupResponse().fromJson(jsonValue, options);
  }

  static fromJsonString(jsonString: string, options?: Partial<JsonReadOptions>): SetupResponse {
    return new SetupResponse().fromJsonString(jsonString, options);
  }

  static equals(a: SetupResponse | PlainMessage<SetupResponse> | undefined, b: SetupResponse | PlainMessage<SetupResponse> | undefined): boolean {
    return proto3.util.equals(SetupResponse, a, b);
  }
}

/**
 * @generated from message haven.Message
 */
export class Message extends Message$1<Message> {
  /**
   * @generated from field: haven.Role role = 1;
   */
  role = Role.ASSISTANT;

  /**
   * @generated from field: string content = 2;
   */
  content = "";

  constructor(data?: PartialMessage<Message>) {
    super();
    proto3.util.initPartial(data, this);
  }

  static readonly runtime: typeof proto3 = proto3;
  static readonly typeName = "haven.Message";
  static readonly fields: FieldList = proto3.util.newFieldList(() => [
    { no: 1, name: "role", kind: "enum", T: proto3.getEnumType(Role) },
    { no: 2, name: "content", kind: "scalar", T: 9 /* ScalarType.STRING */ },
  ]);

  static fromBinary(bytes: Uint8Array, options?: Partial<BinaryReadOptions>): Message {
    return new Message().fromBinary(bytes, options);
  }

  static fromJson(jsonValue: JsonValue, options?: Partial<JsonReadOptions>): Message {
    return new Message().fromJson(jsonValue, options);
  }

  static fromJsonString(jsonString: string, options?: Partial<JsonReadOptions>): Message {
    return new Message().fromJsonString(jsonString, options);
  }

  static equals(a: Message | PlainMessage<Message> | undefined, b: Message | PlainMessage<Message> | undefined): boolean {
    return proto3.util.equals(Message, a, b);
  }
}

/**
 * @generated from message haven.ChatCompletionRequest
 */
export class ChatCompletionRequest extends Message$1<ChatCompletionRequest> {
  /**
   * @generated from field: string worker_name = 1;
   */
  workerName = "";

  /**
   * @generated from field: repeated haven.Message messages = 2;
   */
  messages: Message[] = [];

  /**
   * @generated from field: optional int32 max_tokens = 3;
   */
  maxTokens?: number;

  /**
   * @generated from field: optional float top_p = 4;
   */
  topP?: number;

  /**
   * @generated from field: optional int32 top_k = 5;
   */
  topK?: number;

  /**
   * @generated from field: optional float temperature = 6;
   */
  temperature?: number;

  constructor(data?: PartialMessage<ChatCompletionRequest>) {
    super();
    proto3.util.initPartial(data, this);
  }

  static readonly runtime: typeof proto3 = proto3;
  static readonly typeName = "haven.ChatCompletionRequest";
  static readonly fields: FieldList = proto3.util.newFieldList(() => [
    { no: 1, name: "worker_name", kind: "scalar", T: 9 /* ScalarType.STRING */ },
    { no: 2, name: "messages", kind: "message", T: Message, repeated: true },
    { no: 3, name: "max_tokens", kind: "scalar", T: 5 /* ScalarType.INT32 */, opt: true },
    { no: 4, name: "top_p", kind: "scalar", T: 2 /* ScalarType.FLOAT */, opt: true },
    { no: 5, name: "top_k", kind: "scalar", T: 5 /* ScalarType.INT32 */, opt: true },
    { no: 6, name: "temperature", kind: "scalar", T: 2 /* ScalarType.FLOAT */, opt: true },
  ]);

  static fromBinary(bytes: Uint8Array, options?: Partial<BinaryReadOptions>): ChatCompletionRequest {
    return new ChatCompletionRequest().fromBinary(bytes, options);
  }

  static fromJson(jsonValue: JsonValue, options?: Partial<JsonReadOptions>): ChatCompletionRequest {
    return new ChatCompletionRequest().fromJson(jsonValue, options);
  }

  static fromJsonString(jsonString: string, options?: Partial<JsonReadOptions>): ChatCompletionRequest {
    return new ChatCompletionRequest().fromJsonString(jsonString, options);
  }

  static equals(a: ChatCompletionRequest | PlainMessage<ChatCompletionRequest> | undefined, b: ChatCompletionRequest | PlainMessage<ChatCompletionRequest> | undefined): boolean {
    return proto3.util.equals(ChatCompletionRequest, a, b);
  }
}

/**
 * @generated from message haven.ChatCompletionResponse
 */
export class ChatCompletionResponse extends Message$1<ChatCompletionResponse> {
  /**
   * @generated from field: string text = 1;
   */
  text = "";

  constructor(data?: PartialMessage<ChatCompletionResponse>) {
    super();
    proto3.util.initPartial(data, this);
  }

  static readonly runtime: typeof proto3 = proto3;
  static readonly typeName = "haven.ChatCompletionResponse";
  static readonly fields: FieldList = proto3.util.newFieldList(() => [
    { no: 1, name: "text", kind: "scalar", T: 9 /* ScalarType.STRING */ },
  ]);

  static fromBinary(bytes: Uint8Array, options?: Partial<BinaryReadOptions>): ChatCompletionResponse {
    return new ChatCompletionResponse().fromBinary(bytes, options);
  }

  static fromJson(jsonValue: JsonValue, options?: Partial<JsonReadOptions>): ChatCompletionResponse {
    return new ChatCompletionResponse().fromJson(jsonValue, options);
  }

  static fromJsonString(jsonString: string, options?: Partial<JsonReadOptions>): ChatCompletionResponse {
    return new ChatCompletionResponse().fromJsonString(jsonString, options);
  }

  static equals(a: ChatCompletionResponse | PlainMessage<ChatCompletionResponse> | undefined, b: ChatCompletionResponse | PlainMessage<ChatCompletionResponse> | undefined): boolean {
    return proto3.util.equals(ChatCompletionResponse, a, b);
  }
}

/**
 * @generated from message haven.Model
 */
export class Model extends Message$1<Model> {
  /**
   * @generated from field: string name = 1;
   */
  name = "";

  constructor(data?: PartialMessage<Model>) {
    super();
    proto3.util.initPartial(data, this);
  }

  static readonly runtime: typeof proto3 = proto3;
  static readonly typeName = "haven.Model";
  static readonly fields: FieldList = proto3.util.newFieldList(() => [
    { no: 1, name: "name", kind: "scalar", T: 9 /* ScalarType.STRING */ },
  ]);

  static fromBinary(bytes: Uint8Array, options?: Partial<BinaryReadOptions>): Model {
    return new Model().fromBinary(bytes, options);
  }

  static fromJson(jsonValue: JsonValue, options?: Partial<JsonReadOptions>): Model {
    return new Model().fromJson(jsonValue, options);
  }

  static fromJsonString(jsonString: string, options?: Partial<JsonReadOptions>): Model {
    return new Model().fromJsonString(jsonString, options);
  }

  static equals(a: Model | PlainMessage<Model> | undefined, b: Model | PlainMessage<Model> | undefined): boolean {
    return proto3.util.equals(Model, a, b);
  }
}

/**
 * @generated from message haven.ListModelsResponse
 */
export class ListModelsResponse extends Message$1<ListModelsResponse> {
  /**
   * @generated from field: repeated haven.Model models = 1;
   */
  models: Model[] = [];

  constructor(data?: PartialMessage<ListModelsResponse>) {
    super();
    proto3.util.initPartial(data, this);
  }

  static readonly runtime: typeof proto3 = proto3;
  static readonly typeName = "haven.ListModelsResponse";
  static readonly fields: FieldList = proto3.util.newFieldList(() => [
    { no: 1, name: "models", kind: "message", T: Model, repeated: true },
  ]);

  static fromBinary(bytes: Uint8Array, options?: Partial<BinaryReadOptions>): ListModelsResponse {
    return new ListModelsResponse().fromBinary(bytes, options);
  }

  static fromJson(jsonValue: JsonValue, options?: Partial<JsonReadOptions>): ListModelsResponse {
    return new ListModelsResponse().fromJson(jsonValue, options);
  }

  static fromJsonString(jsonString: string, options?: Partial<JsonReadOptions>): ListModelsResponse {
    return new ListModelsResponse().fromJsonString(jsonString, options);
  }

  static equals(a: ListModelsResponse | PlainMessage<ListModelsResponse> | undefined, b: ListModelsResponse | PlainMessage<ListModelsResponse> | undefined): boolean {
    return proto3.util.equals(ListModelsResponse, a, b);
  }
}

/**
 * @generated from message haven.Worker
 */
export class Worker extends Message$1<Worker> {
  /**
   * @generated from field: string worker_name = 1;
   */
  workerName = "";

  /**
   * @generated from field: haven.Status status = 2;
   */
  status = Status.ONLINE;

  constructor(data?: PartialMessage<Worker>) {
    super();
    proto3.util.initPartial(data, this);
  }

  static readonly runtime: typeof proto3 = proto3;
  static readonly typeName = "haven.Worker";
  static readonly fields: FieldList = proto3.util.newFieldList(() => [
    { no: 1, name: "worker_name", kind: "scalar", T: 9 /* ScalarType.STRING */ },
    { no: 2, name: "status", kind: "enum", T: proto3.getEnumType(Status) },
  ]);

  static fromBinary(bytes: Uint8Array, options?: Partial<BinaryReadOptions>): Worker {
    return new Worker().fromBinary(bytes, options);
  }

  static fromJson(jsonValue: JsonValue, options?: Partial<JsonReadOptions>): Worker {
    return new Worker().fromJson(jsonValue, options);
  }

  static fromJsonString(jsonString: string, options?: Partial<JsonReadOptions>): Worker {
    return new Worker().fromJsonString(jsonString, options);
  }

  static equals(a: Worker | PlainMessage<Worker> | undefined, b: Worker | PlainMessage<Worker> | undefined): boolean {
    return proto3.util.equals(Worker, a, b);
  }
}

/**
 * @generated from message haven.ListWorkersResponse
 */
export class ListWorkersResponse extends Message$1<ListWorkersResponse> {
  /**
   * @generated from field: repeated haven.Worker workers = 1;
   */
  workers: Worker[] = [];

  constructor(data?: PartialMessage<ListWorkersResponse>) {
    super();
    proto3.util.initPartial(data, this);
  }

  static readonly runtime: typeof proto3 = proto3;
  static readonly typeName = "haven.ListWorkersResponse";
  static readonly fields: FieldList = proto3.util.newFieldList(() => [
    { no: 1, name: "workers", kind: "message", T: Worker, repeated: true },
  ]);

  static fromBinary(bytes: Uint8Array, options?: Partial<BinaryReadOptions>): ListWorkersResponse {
    return new ListWorkersResponse().fromBinary(bytes, options);
  }

  static fromJson(jsonValue: JsonValue, options?: Partial<JsonReadOptions>): ListWorkersResponse {
    return new ListWorkersResponse().fromJson(jsonValue, options);
  }

  static fromJsonString(jsonString: string, options?: Partial<JsonReadOptions>): ListWorkersResponse {
    return new ListWorkersResponse().fromJsonString(jsonString, options);
  }

  static equals(a: ListWorkersResponse | PlainMessage<ListWorkersResponse> | undefined, b: ListWorkersResponse | PlainMessage<ListWorkersResponse> | undefined): boolean {
    return proto3.util.equals(ListWorkersResponse, a, b);
  }
}

/**
 * @generated from message haven.CreateInferenceWorkerRequest
 */
export class CreateInferenceWorkerRequest extends Message$1<CreateInferenceWorkerRequest> {
  /**
   * @generated from field: string model_name = 1;
   */
  modelName = "";

  /**
   * @generated from field: string quantization = 2;
   */
  quantization = "";

  /**
   * @generated from field: optional string worker_name = 3;
   */
  workerName?: string;

  /**
   * @generated from field: optional haven.GpuType gpu_type = 4;
   */
  gpuType?: GpuType;

  /**
   * @generated from field: optional int32 gpu_count = 6;
   */
  gpuCount?: number;

  /**
   * @generated from field: optional string zone = 7;
   */
  zone?: string;

  constructor(data?: PartialMessage<CreateInferenceWorkerRequest>) {
    super();
    proto3.util.initPartial(data, this);
  }

  static readonly runtime: typeof proto3 = proto3;
  static readonly typeName = "haven.CreateInferenceWorkerRequest";
  static readonly fields: FieldList = proto3.util.newFieldList(() => [
    { no: 1, name: "model_name", kind: "scalar", T: 9 /* ScalarType.STRING */ },
    { no: 2, name: "quantization", kind: "scalar", T: 9 /* ScalarType.STRING */ },
    { no: 3, name: "worker_name", kind: "scalar", T: 9 /* ScalarType.STRING */, opt: true },
    { no: 4, name: "gpu_type", kind: "enum", T: proto3.getEnumType(GpuType), opt: true },
    { no: 6, name: "gpu_count", kind: "scalar", T: 5 /* ScalarType.INT32 */, opt: true },
    { no: 7, name: "zone", kind: "scalar", T: 9 /* ScalarType.STRING */, opt: true },
  ]);

  static fromBinary(bytes: Uint8Array, options?: Partial<BinaryReadOptions>): CreateInferenceWorkerRequest {
    return new CreateInferenceWorkerRequest().fromBinary(bytes, options);
  }

  static fromJson(jsonValue: JsonValue, options?: Partial<JsonReadOptions>): CreateInferenceWorkerRequest {
    return new CreateInferenceWorkerRequest().fromJson(jsonValue, options);
  }

  static fromJsonString(jsonString: string, options?: Partial<JsonReadOptions>): CreateInferenceWorkerRequest {
    return new CreateInferenceWorkerRequest().fromJsonString(jsonString, options);
  }

  static equals(a: CreateInferenceWorkerRequest | PlainMessage<CreateInferenceWorkerRequest> | undefined, b: CreateInferenceWorkerRequest | PlainMessage<CreateInferenceWorkerRequest> | undefined): boolean {
    return proto3.util.equals(CreateInferenceWorkerRequest, a, b);
  }
}

/**
 * @generated from message haven.InferenceWorker
 */
export class InferenceWorker extends Message$1<InferenceWorker> {
  /**
   * @generated from field: string worker_name = 1;
   */
  workerName = "";

  constructor(data?: PartialMessage<InferenceWorker>) {
    super();
    proto3.util.initPartial(data, this);
  }

  static readonly runtime: typeof proto3 = proto3;
  static readonly typeName = "haven.InferenceWorker";
  static readonly fields: FieldList = proto3.util.newFieldList(() => [
    { no: 1, name: "worker_name", kind: "scalar", T: 9 /* ScalarType.STRING */ },
  ]);

  static fromBinary(bytes: Uint8Array, options?: Partial<BinaryReadOptions>): InferenceWorker {
    return new InferenceWorker().fromBinary(bytes, options);
  }

  static fromJson(jsonValue: JsonValue, options?: Partial<JsonReadOptions>): InferenceWorker {
    return new InferenceWorker().fromJson(jsonValue, options);
  }

  static fromJsonString(jsonString: string, options?: Partial<JsonReadOptions>): InferenceWorker {
    return new InferenceWorker().fromJsonString(jsonString, options);
  }

  static equals(a: InferenceWorker | PlainMessage<InferenceWorker> | undefined, b: InferenceWorker | PlainMessage<InferenceWorker> | undefined): boolean {
    return proto3.util.equals(InferenceWorker, a, b);
  }
}

