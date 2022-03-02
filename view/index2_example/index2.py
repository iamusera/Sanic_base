import os
import pandas as pd
from grpclib.client import Channel

from sanic import Blueprint, json
from celery.result import AsyncResult
from extensions.init_db import engine
from extensions.init_celery_tasks import task_async
from extensions.init_logger import TEST_LOGGER

from view.index2_example.serializer import timmer
from view.grpc_service.proto.hello_pb2 import HelloRequest
from view.grpc_service.proto.hello_grpc import HelloStub


index_2 = Blueprint('index2_example', url_prefix='index_2')


@timmer
async def ti_2():
    sql = """ select * from etl_lev1 where rownum <= 10 """
    with engine.begin() as con:
        df = pd.read_sql(sql, engine)
        print(df)
    TEST_LOGGER.info(msg='test logger')
    return


@index_2.route("/decorator_index2")
async def test(request):
    b = await ti_2()
    return json({'status': b})


@index_2.route("/async_tasks")
async def test_async(request):
    """ celery 测试 """
    b = task_async.delay(1, 2)
    return json({'status': b.task_id})


@index_2.route("/c_result/<task_id:string>")
async def get_celery_result(request, task_id):
    """ 根据celery task id 查询任务进度和结果 """
    res = AsyncResult(task_id)
    return json({'result': res.result})


data = """
{
    "id": 'test grpc'
}
"""

@index_2.route("/grpc")
async def get_celery_result(request):
    """ 异步grpc 请求 """
    channel = Channel(host=os.getenv('GRPC_LISTEN_ADDR', '127.0.0.1'),
                      port=os.getenv('GRPC_LISTEN_PORT', 8990)
                      )
    stub = HelloStub(channel)
    res = await stub.hello_action(HelloRequest(action=data))
    channel.close()
    return json({'result': res.message})


#