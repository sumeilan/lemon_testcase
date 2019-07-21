#http://lemondream.chumanapp.com/api/user/profile
# 用户信息

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

    def test_user_profile(self):
        token = file_operation.read_file('token.json')
        body = {'access_token':token['access_token']}
        # print(json.dumps(body))
        HmacSHA256.sh256(json.dumps(body))

        path = '/api/user/profile'
        url = readConfig.ReadConfig.get_http('baseurl') + path

        try:
            headers = file_operation.read_file('headers.json')
            response = requests.post(url, json=body, headers=headers, verify=False)
            # print(response.text)
            datas = response.json()['data']
        except Exception as e:
            print('出错了:',e)

        assert_that(response.json()['code']).is_equal_to(0)
        assert_that(datas['id']).is_equal_to(1042)
        assert_that(datas['nickname']).is_not_none()


if __name__ == '__main__':
    unittest.main()
