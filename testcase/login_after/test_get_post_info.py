#http://lemondream.chumanapp.com/api/post/get_post_info
# 阅读帖子

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

    @data('1906240266')
    def test_get_comic_single_info(self, value):
        token = file_operation.read_file('token.json')
        body = {'post_id':value,'access_token':token['access_token']}
        # print(json.dumps(body))
        HmacSHA256.sh256(json.dumps(body))

        path = '/api/post/get_post_info'
        url = readConfig.ReadConfig.get_http('baseurl') + path

        try:
	        headers = file_operation.read_file('headers.json')
	        response = requests.post(url, json=body, headers=headers, verify=False)
	        # print(response.text)
	        single_info = response.json()['data']['info']
        except Exception as e:
	        print('出错了:', e)

        assert_that(response.json()['code']).is_equal_to(0)
        assert_that(single_info['content']).is_not_none()

if __name__ == '__main__':
    unittest.main()
