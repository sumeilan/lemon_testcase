#http://lemondream.chumanapp.com/api/user/check_nickname_disabled_word   检查是否有禁词

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

    @data('SB')
    def test_check_nickname_disabled_word(self,nickname):
        token = file_operation.read_file('token.json')
        body = {'access_token':token['access_token'],'title':nickname}
        # print(json.dumps(body))
        HmacSHA256.sh256(json.dumps(body))

        path = '/api/user/check_nickname_disabled_word'
        url = readConfig.ReadConfig.get_http('baseurl') + path

        try:
	        headers = file_operation.read_file('headers.json')
	        response = requests.post(url, json=body, headers=headers, verify=False)
	        print(response.text)
	        datas = response.json()['data']
	        if datas['status']:
		        print('没有禁词')
	        else:
		        print('包含禁词')

        except Exception as e:
	        print('出错了:', e)

        assert_that(response.json()['code']).is_equal_to(0)



if __name__ == '__main__':
    unittest.main()
