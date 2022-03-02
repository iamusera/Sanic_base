"""
序列化与接口参数验证
"""
from extensions.init_logger import TEST_LOGGER
import time


def timmer(func):
    def deco(*args, **kwargs):
        print('\n函数：{_funcname_}开始运行：'.format(_funcname_=func.__name__))
        TEST_LOGGER.info('\n函数：{_funcname_}开始运行：'.format(_funcname_=func.__name__))
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        print('函数:{_funcname_}运行了 {_time_}秒'.format(_funcname_=func.__name__, _time_=(end_time - start_time)))
        TEST_LOGGER.info(('函数:{_funcname_}运行了 {_time_}秒'.format(_funcname_=func.__name__, _time_=(end_time - start_time))))
        return res

    return deco
