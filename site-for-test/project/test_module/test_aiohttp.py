import json

from ..models import SomeObject, SomeObjectEncoder
from ..client import get_response, post_response

cat1 = SomeObject(state=True)
mock_data_str = json.dumps(cat1, indent=4, cls=SomeObjectEncoder)
mock_data = json.loads(mock_data_str)
url = 'http://192.168.88.232:24'


async def test_get_resource():
    resp = await get_response()

    assert resp.status == 200


async def test_post_resource():
    resp = await post_response()

    assert resp.status == 200


