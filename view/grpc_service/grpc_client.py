import grpc

from view.grpc_service.proto import hello_pb2, hello_grpc

data = """
{
    "id": 1
}
"""


def run():
    channel = grpc.insecure_channel("localhost:8990")
    stub = hello_grpc.HelloStub(channel)
    response = stub.hello_action(hello_pb2.HelloRequest(action=data))
    print("Hello result received:  %s" % response.message)
    return "Hello result received:  %s" % response.message


# if __name__ == '__main__':
#     run()
