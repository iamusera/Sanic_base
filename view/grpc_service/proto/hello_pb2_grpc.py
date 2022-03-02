# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from view.grpc_service.proto import hello_pb2 as hello__pb2


class HelloStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.hello_action = channel.unary_unary(
                '/sample.Hello/hello_action',
                request_serializer=hello__pb2.HelloRequest.SerializeToString,
                response_deserializer=hello__pb2.HelloResponse.FromString,
                )


class HelloServicer(object):
    """Missing associated documentation comment in .proto file."""

    def hello_action(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_HelloServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'hello_action': grpc.unary_unary_rpc_method_handler(
                    servicer.hello_action,
                    request_deserializer=hello__pb2.HelloRequest.FromString,
                    response_serializer=hello__pb2.HelloResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'sample.Hello', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Hello(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def hello_action(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sample.Hello/hello_action',
            hello__pb2.HelloRequest.SerializeToString,
            hello__pb2.HelloResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
