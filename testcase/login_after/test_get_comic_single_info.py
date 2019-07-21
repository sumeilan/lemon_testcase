# http://lemondream.chumanapp.com/api/comic/get_comic_single_info
# 阅读漫画单篇

import requests
import unittest

from base import HmacSHA256, file_operation
import json
from config import readConfig
from ddt import ddt, data
from assertpy import assert_that

@ddt
class MyTestSuite(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @data('48283683')
    def test_get_comic_single_info(self, value):
        token = file_operation.read_file('token.json')
        body = {'comic_id':value,'access_token':token['access_token']}
        # print(json.dumps(body))
        HmacSHA256.sh256(json.dumps(body))

        path = '/api/comic/get_comic_single_info'
        url = readConfig.ReadConfig.get_http('baseurl') + path

        try:
	        headers = file_operation.read_file('headers.json')
	        response = requests.post(url, json=body, headers=headers, verify=False)
	        # print(response.text)
        except Exception as e:
	        print('出错了:', e)
        assert_that(response.json()['code']).is_equal_to(0)
        single_info = response.json()['data']['single_info']
        assert_that(single_info['author_id']).is_not_none()
        assert_that(single_info['data_json']).is_not_none()



if __name__ == '__main__':
    unittest.main()
