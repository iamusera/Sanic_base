from sanic.views import HTTPMethodView
from sanic.response import text


class ViewWithDecorator(HTTPMethodView):
    # decorators = [some_decorator_here]  所有方法都被装饰
    # or 仅装饰get方法
    # @staticmethod
    # @some_decorator_here
    def get(self, request, name):
        return text('Hello I have a decorator')

    def post(self, request, name):
        return text("Hello I also have a decorator")


# app.add_route(ViewWithDecorator.as_view(), '/decorator_class_view')
