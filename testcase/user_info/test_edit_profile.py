# http://lemondream.chumanapp.com/api/user/edit_profile  编辑个人资料

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

    @data('588')
    def test_edit_profile(self, nickname):
        token = file_operation.read_file('token.json')
        body = {
            'access_token': token['access_token'],
            'birthday': '2000-01-01',
            'city': '',
            'nickname': nickname,
            'province': '',
            'sex': 3}
        # print(json.dumps(body))
        HmacSHA256.sh256(json.dumps(body))

        path = '/api/user/edit_profile'
        url = readConfig.ReadConfig.get_http('baseurl') + path

        try:
            headers = file_operation.read_file('headers.json')
            response = requests.post(
                url, json=body, headers=headers, verify=False)
            print(response.text)
            datas = response.json()

        except Exception as e:
            print('出错了:', e)

        assert_that(response.json()['code']).is_equal_to(0)
        assert_that(datas['msg']).is_equal_to('请求成功')



if __name__ == '__main__':
    unittest.main()
