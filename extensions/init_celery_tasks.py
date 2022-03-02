from extensions.init_celery import my_celery


@my_celery.task(bind=True)
def task_10_seconds(self, a: int, b: int):
    return a + b


@my_celery.task(bind=True)
def task_24_hour(self, a: int, b: int):
    return a + b


@my_celery.task(bind=True)
def task_async(self, a: int, b: int):

    return a + b
