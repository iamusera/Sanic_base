import os
import asyncio

from grpclib.client import Channel

from view.grpc_service.proto.hello_pb2 import HelloRequest
from view.grpc_service.proto.hello_grpc import HelloStub

data = """
{
    "id": 1
}
"""


async def asy_grpc():
    channel = Channel(host=os.getenv('GRPC_LISTEN_ADDR', '127.0.0.1'),
                      port=os.getenv('GRPC_LISTEN_PORT', 8990)
                      )
    stub = HelloStub(channel)
    print(await stub.hello_action(HelloRequest(action=data)))
    channel.close()

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(asy_grpc())
