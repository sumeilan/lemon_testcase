#http://lemondream.chumanapp.com/api/user/third_login

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

    def test_third_login(self):
        config_path = readConfig.ReadConfig.get_config_path('path')
        body = {'avatar':'http://thirdqq.qlogo.cn/g?b=oidb&k=edlgyevh0NKzuOHe2SX6yg&s=100','birthday':'2000-01-01','city':'','device':1,'nickname':'ssk','openid':'FD717EC03696FFB9E78AADEC85E6565D','province':'','sex':2,'type':2}
        HmacSHA256.sh256(json.dumps(body))

        path = '/api/user/third_login'
        url = readConfig.ReadConfig.get_http('baseurl') + path

        headers = file_operation.read_file('headers.json')
        try:
            response = requests.post(url, json=body, headers=headers, verify=False)
            datas = response.json()['data']
            token = {'access_token': datas['access_token'],'refresh_token':datas['refresh_token']}
            print(response.text)
            file_operation.write_file(token, 'token.json')
        except Exception as e:
            print('出错了:', e)
        assert_that(response.json()['code']).is_equal_to(0)

        assert_that(datas['uid']).is_equal_to(1042)
        assert_that(datas['is_bind']).is_equal_to(1)

if __name__ == '__main__':
    unittest.main()
