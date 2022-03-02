from sanic import Blueprint
from view.index_example import index
from view.index2_example import index_2


def register_view():
    api = Blueprint.group(index, index_2)
    return api
