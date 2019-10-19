#http://api-lemon.chumanapp.com/api/voice_template/get_tab_list

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

    def test_get_tab_list(self):
        token = file_operation.read_file('token.json')
        body = {'access_token':token['access_token'],'page':'1','pagesize':'20'}
        HmacSHA256.sh256(json.dumps(body))

        path = '/api/voice_template/get_tab_list'
        url = readConfig.ReadConfig.get_http('baseurl') + path

        try:
            headers = file_operation.read_file('headers.json')
            response = requests.post(url, json=body, headers=headers, verify=False)

        except Exception as e:
            print('出错了:',e)

        assert_that(response.status_code).is_equal_to(200)


if __name__ == '__main__':
    unittest.main()
