import os
import logging
from sanic import Sanic
from view import register_view
from extensions.init_celery import register_celery, my_celery
from extensions.init_logger import init_log
from extensions.init_dotenv import init_dotenv
from view.class_view_example import ViewWithDecorator


def creat_app():
    app = Sanic(__name__)
    app_setting(app)
    app.blueprint(register_view())
    app.add_route(ViewWithDecorator.as_view(), '/decorator_class_view')
    return app


def app_setting(app):
    init_dotenv()
    init_log()
    app.config.update(os.environ)
    register_celery(celery=my_celery, app=app)