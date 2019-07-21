# http://lemondream.chumanapp.com/api/user/check_nickname 修改昵称检查


import requests
import unittest

from base import HmacSHA256, file_operation
import json
from config import readConfig
from ddt import ddt, data
import os
from assertpy import assert_that


@ddt
class MyTestSuite(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @data('ssk8')
    def test_check_nickname(self, nickname):
        token = file_operation.read_file('token.json')
        body = {'access_token': token['access_token'], 'nickname': nickname}
        # print(json.dumps(body))
        HmacSHA256.sh256(json.dumps(body))

        path = '/api/user/check_nickname'
        url = readConfig.ReadConfig.get_http('baseurl') + path

        try:
	        headers = file_operation.read_file('headers.json')
	        response = requests.post(url, json=body, headers=headers, verify=False)
	        print(response.text)
	        datas = response.json()['data']

	        if datas['is_used'] == 0:
		        print('可以调用编辑昵称接口')
	        elif datas['is_used'] == 1:
		        print('昵称已被占用')
        except Exception as e:
            print('出错了:',e)

        assert_that(response.json()['code']).is_equal_to(0)


if __name__ == '__main__':
    unittest.main()
