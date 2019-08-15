# http://api.lemondream.cn/api/External/get_external_content_info

import requests
import unittest
from base import HmacSHA256, get_response_value, file_operation
import json
from config import readConfig
from ddt import ddt, data, file_data
from assertpy import assert_that


@ddt
class MyTestSuite(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @file_data(r"D:\pycharm\lemon_testcase\config\datas.json")
    def test_get_external_content_info(self, value):
        body = {'content_id': 190648615}
        HmacSHA256.sh256(json.dumps(body))

        path = '/api/External/get_external_content_info'
        url = readConfig.ReadConfig.get_http('baseurl') + path
        try:
            headers = file_operation.read_file('headers.json')
            response = requests.post(
                url, json=body, headers=headers, verify=False)
            # print(response.text)

        except Exception as e:
            print('出错了:', e)
        assert_that(response.json()['code']).is_equal_to(0)

        single_info = response.json()['data']['info']
        assert_that(single_info['content']).is_not_none()


if __name__ == '__main__':
    unittest.main()
