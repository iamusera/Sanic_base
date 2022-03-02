from sanic import Blueprint
from sanic.response import json
index = Blueprint('index_example')


@index.route('/')
async def bp_root(request):
    return json({'my': 'blueprint'})