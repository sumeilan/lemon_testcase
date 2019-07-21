# http://139.9.213.120/api/recommend/get_recommend_content_list

import requests
import unittest

from base import HmacSHA256, get_response_value, file_operation
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

    @data('1')
    def test_recommend_login(self, page):
        token = file_operation.read_file('token.json')
        body = {
            'page': page,
            'pageSize': '20',
            'app_key': 'lemondream',
            'access_token': token['access_token']}
        # print(json.dumps(body))
        HmacSHA256.sh256(json.dumps(body))

        path = '/api/recommend/get_recommend_content_list'
        url = readConfig.ReadConfig.get_http('baseurl') + path

        try:
            headers = file_operation.read_file('headers.json')
            response = requests.post(url, json=body, headers=headers, verify=False)
            # print(response.text)
            dataList = response.json()['data']
            obj_ids = get_response_value.get_target_value('obj_id', dataList, [])
            obj_id = {"obj_id": obj_ids[0]}
            file_operation.write_file(obj_id, 'datas.json')

            tpyes = get_response_value.get_target_value('type', dataList, [])
        except Exception as e:
            print('出错了:', e)

        assert_that(response.json()['code']).is_equal_to(0)
        for i in range(0, len(tpyes)):
            assert_that(tpyes[i]).is_not_empty()
            assert_that(tpyes[i]).is_type_of(str)
            assert_that(['1', '2', '4', '7', '8', '9', '10']
                        ).contains(tpyes[i])


if __name__ == '__main__':
    unittest.main()
