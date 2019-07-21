# http://139.9.213.120/api/recommend/get_recommend_content_list

import requests
import unittest

from base import HmacSHA256
import json
from config import readConfig
from ddt import ddt,data

@ddt
class MyTestSuite(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @data(1)
    def test_recommend_content(self,page):
        body = {"page": "1", "pageSize": "20", "app_key": "lemondream"}
        HmacSHA256.sh256(json.dumps(body))

        path = '/api/recommend/get_recommend_content_list'
        url = readConfig.ReadConfig.get_http('baseurl') + path

        with open("../config/headers.json", 'r') as load_f:
	        headers = json.load(load_f)
        print(headers)
        response = requests.post(url, json=body, headers=headers, verify=False)
        status = response.json()['msg']
        self.assertEqual(status, '请求成功')
        print(response.text)

if __name__ == '__main__':
    unittest.main()
