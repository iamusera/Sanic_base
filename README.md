###  sanic

```
from sanic import Sanic
from sanic.response import json

app = Sanic()

@app.route("/")
async def test(request):
    return json({"hello": "world"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
```

#####项目结构

```
sanic_frame
|--etc 日志配置文件
|--extensions
	|--db   数据库
	|--logger 日志
	|--base_model 操作成功和失败返回
|-- view 试图函数
	|--grpc_service grpc demo，异步请求
	|--index 视图示例
		|--index_page 视图函数文件
		|--serializer 视图函数序列化与接口验证
	|-- init.py 注册试图
|.env 环境配置
|app.py 注册app
|main.py 程序入口
	
```

##### celery启动

```
celery -A extensions.init_celery.my_celery worker -P eventlet
   或者定时任务启动
celery beat -A extensions.celery_app.init_celery.my_celery -l=info --logfile="/celery_scehe"

```

#####GRPC  异步请求

```
cd /sanic_base/view/grpc_service/proto
执行 python37 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. --grpclib_python_out=. hello.proto 

详见：https://github.com/vmagamedov/grpclib
```



##### 功能

```
1. 日志
2. oracle连接
3. celery，基于redis
4. redis pool
5. 支持grpc异步请求
```

######启动

```
cd /sanic_base
python3 main.py
  # 测试grpc
  cd /sanic_base/view/grpc_service
  python grpc_server.py
  python grpc_asyncio_client.py
```

#####测试url

```
http://127.0.0.1:8080/index_2/grpc  		grpc
http://127.0.0.1:8080/index_2/async_tasks  	获取celery任务ID
http://127.0.0.1:8080/index_2/c_result/<task_id>  参数url，查询celery任务结果
```

