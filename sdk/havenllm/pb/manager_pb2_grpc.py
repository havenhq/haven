# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import manager_pb2 as manager__pb2


class HavenStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Setup = channel.unary_unary(
                '/haven.Haven/Setup',
                request_serializer=manager__pb2.SetupRequest.SerializeToString,
                response_deserializer=manager__pb2.Empty.FromString,
                )
        self.Generate = channel.unary_stream(
                '/haven.Haven/Generate',
                request_serializer=manager__pb2.GenerateRequest.SerializeToString,
                response_deserializer=manager__pb2.GenerateResponse.FromString,
                )
        self.ListModels = channel.unary_unary(
                '/haven.Haven/ListModels',
                request_serializer=manager__pb2.Empty.SerializeToString,
                response_deserializer=manager__pb2.ListModelsResponse.FromString,
                )
        self.AddModel = channel.unary_unary(
                '/haven.Haven/AddModel',
                request_serializer=manager__pb2.AddModelRequest.SerializeToString,
                response_deserializer=manager__pb2.Empty.FromString,
                )
        self.DeleteModel = channel.unary_unary(
                '/haven.Haven/DeleteModel',
                request_serializer=manager__pb2.ModelName.SerializeToString,
                response_deserializer=manager__pb2.Empty.FromString,
                )
        self.CreateInferenceWorker = channel.unary_unary(
                '/haven.Haven/CreateInferenceWorker',
                request_serializer=manager__pb2.CreateInferenceWorkerRequest.SerializeToString,
                response_deserializer=manager__pb2.InferenceWorker.FromString,
                )
        self.PauseInferenceWorker = channel.unary_unary(
                '/haven.Haven/PauseInferenceWorker',
                request_serializer=manager__pb2.InferenceWorker.SerializeToString,
                response_deserializer=manager__pb2.InferenceWorker.FromString,
                )
        self.ResumeInferenceWorker = channel.unary_unary(
                '/haven.Haven/ResumeInferenceWorker',
                request_serializer=manager__pb2.InferenceWorker.SerializeToString,
                response_deserializer=manager__pb2.InferenceWorker.FromString,
                )
        self.DeleteInferenceWorker = channel.unary_unary(
                '/haven.Haven/DeleteInferenceWorker',
                request_serializer=manager__pb2.InferenceWorker.SerializeToString,
                response_deserializer=manager__pb2.InferenceWorker.FromString,
                )


class HavenServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Setup(self, request, context):
        """Setup (first time starting the manager)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Generate(self, request, context):
        """Generate text from a prompt.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListModels(self, request, context):
        """Get the list of models and their descriptions.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddModel(self, request, context):
        """Model management.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteModel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateInferenceWorker(self, request, context):
        """Inference worker management.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PauseInferenceWorker(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ResumeInferenceWorker(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteInferenceWorker(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_HavenServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Setup': grpc.unary_unary_rpc_method_handler(
                    servicer.Setup,
                    request_deserializer=manager__pb2.SetupRequest.FromString,
                    response_serializer=manager__pb2.Empty.SerializeToString,
            ),
            'Generate': grpc.unary_stream_rpc_method_handler(
                    servicer.Generate,
                    request_deserializer=manager__pb2.GenerateRequest.FromString,
                    response_serializer=manager__pb2.GenerateResponse.SerializeToString,
            ),
            'ListModels': grpc.unary_unary_rpc_method_handler(
                    servicer.ListModels,
                    request_deserializer=manager__pb2.Empty.FromString,
                    response_serializer=manager__pb2.ListModelsResponse.SerializeToString,
            ),
            'AddModel': grpc.unary_unary_rpc_method_handler(
                    servicer.AddModel,
                    request_deserializer=manager__pb2.AddModelRequest.FromString,
                    response_serializer=manager__pb2.Empty.SerializeToString,
            ),
            'DeleteModel': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteModel,
                    request_deserializer=manager__pb2.ModelName.FromString,
                    response_serializer=manager__pb2.Empty.SerializeToString,
            ),
            'CreateInferenceWorker': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateInferenceWorker,
                    request_deserializer=manager__pb2.CreateInferenceWorkerRequest.FromString,
                    response_serializer=manager__pb2.InferenceWorker.SerializeToString,
            ),
            'PauseInferenceWorker': grpc.unary_unary_rpc_method_handler(
                    servicer.PauseInferenceWorker,
                    request_deserializer=manager__pb2.InferenceWorker.FromString,
                    response_serializer=manager__pb2.InferenceWorker.SerializeToString,
            ),
            'ResumeInferenceWorker': grpc.unary_unary_rpc_method_handler(
                    servicer.ResumeInferenceWorker,
                    request_deserializer=manager__pb2.InferenceWorker.FromString,
                    response_serializer=manager__pb2.InferenceWorker.SerializeToString,
            ),
            'DeleteInferenceWorker': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteInferenceWorker,
                    request_deserializer=manager__pb2.InferenceWorker.FromString,
                    response_serializer=manager__pb2.InferenceWorker.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'haven.Haven', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Haven(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Setup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/haven.Haven/Setup',
            manager__pb2.SetupRequest.SerializeToString,
            manager__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Generate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/haven.Haven/Generate',
            manager__pb2.GenerateRequest.SerializeToString,
            manager__pb2.GenerateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListModels(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/haven.Haven/ListModels',
            manager__pb2.Empty.SerializeToString,
            manager__pb2.ListModelsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddModel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/haven.Haven/AddModel',
            manager__pb2.AddModelRequest.SerializeToString,
            manager__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteModel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/haven.Haven/DeleteModel',
            manager__pb2.ModelName.SerializeToString,
            manager__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateInferenceWorker(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/haven.Haven/CreateInferenceWorker',
            manager__pb2.CreateInferenceWorkerRequest.SerializeToString,
            manager__pb2.InferenceWorker.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PauseInferenceWorker(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/haven.Haven/PauseInferenceWorker',
            manager__pb2.InferenceWorker.SerializeToString,
            manager__pb2.InferenceWorker.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ResumeInferenceWorker(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/haven.Haven/ResumeInferenceWorker',
            manager__pb2.InferenceWorker.SerializeToString,
            manager__pb2.InferenceWorker.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteInferenceWorker(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/haven.Haven/DeleteInferenceWorker',
            manager__pb2.InferenceWorker.SerializeToString,
            manager__pb2.InferenceWorker.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
