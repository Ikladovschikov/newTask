import json

from aiohttp_serv.models import SomeObject
from aiohttp_serv.client import get_response, post_response


cat1 = SomeObject(True)
mock_data_str = json.dumps(cat1.__dict__)
mock_data_dict = json.loads(mock_data_str)
URL = 'http://0.0.0.0:8080'


async def test_get_resource():
    resp = await get_response()
    assert resp.status == 200


async def test_post_resource():
    resp = await post_response()
    assert resp.status == 200
