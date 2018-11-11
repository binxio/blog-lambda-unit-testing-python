from lambdas.python_function import *
from tests import *


def test_python_function():
    resp = handler(api_gateway_event({}), None)
    assert resp == {'statusCode': 200, 'body': '"Hello Python"'}

