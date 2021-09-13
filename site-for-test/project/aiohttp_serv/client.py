import json

import aiohttp
import asyncio
from models import SomeObject

URL = 'http://0.0.0.0:8080'
cat1 = SomeObject(True)
mock_data = json.dumps(cat1.__dict__)


async def get_response():
    async with aiohttp.ClientSession() as session:
        async with session.get(url=URL, timeout=10000) as resp:
            print(resp.status)
            return resp


async def post_response():
    async with aiohttp.ClientSession() as session:
        async with session.post(url=URL, timeout=10000, data=mock_data) as resp:
            print(resp.status)
            return resp


loop = asyncio.get_event_loop()
loop.run_until_complete(get_response())
loop.run_until_complete(post_response())
