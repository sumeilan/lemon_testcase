# http://api.lemondream.cn/api/External/get_external_content_info

import requests
import unittest
from base import HmacSHA256, file_operation
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

    @data('1906179','190627817')
    def test_get_external_content_info(self, value):
        token = file_operation.read_file('token.json')
        body = {'content_id': value, 'access_token': token['access_token']}
        HmacSHA256.sh256(json.dumps(body))

        path = '/api/External/get_external_content_info'
        url = readConfig.ReadConfig.get_http('baseurl') + path

        try:
            headers = file_operation.read_file('headers.json')
            response = requests.post(url, json=body, headers=headers, verify=False)
            info = response.json()['data']['info']
            print(info['video_obj'])

        except Exception as e:
	        print('出错了:', e)

        assert_that(response.json()['code']).is_equal_to(0)
        if info['type'] == 2:
            assert_that(info['type']).is_not_none()
            assert_that(info['video_obj']).contains_entry({'max_height': 1280}, {'max_width': 720})
        elif type  == 1:
	        assert_that(info['video_obj']).is_empty()



if __name__ == '__main__':
    unittest.main()
