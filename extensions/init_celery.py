import os
from celery import Celery
from etc import celery_config


def register_celery(celery, app):
    class ContextTask(celery.Task):
        abstract = True

        def __call__(self, *args, **kwargs):
            # with app.app_context():
            with app.ctx:
                return self.run(*args, **kwargs)

    celery.Task = ContextTask


def make_celery(app_name):
    celery = Celery(app_name, broker=os.getenv('BROKER_URL', 'redis://127.0.0.1:6379/1'),
                    backend=os.getenv('CELERY_RESULT_BACKEND', 'redis://127.0.0.1:6379/2'))
    celery.config_from_object(celery_config)

    return celery


my_celery = make_celery(__name__)
