import json, requests
from unittest.main import main
from aiohttp.client import request
from django.test import TestCase
from project.views import *






class Test(TestCase):


    def test_connect(self):
        response = requests.get('http://0.0.0.0:8080')
        assert response.status_code == 200


    def test_states_is_equal(self):
        # data = {'state':False}
        # assert cat2.state == data['state']
        data = {'state':True}
        request = json.dumps(data)
        result = get_post(request)
        self.assertEqual(result, True)

