#http://lemon_config2.chumanapp.com/demo.php?system=android&version=0.6.0  config文件

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

    @data('0.9.1', '0.9.0')
    def test_config2(self,version):
        path = '/config.php?system=android&version=' + version
        url = readConfig.ReadConfig.get_http('config_url') + path

        try:
            response = requests.get(url,  verify=False)
            # print(response.text)
            datas = response.json()['data']

        except Exception as e:
	        print('出错了:', e)
        assert_that(response.json()['status']).is_equal_to('ok')
        assert_that(datas['api_host']).is_in('http://lemondream.chumanapp.com/', 'http://api-lemon.chumanapp.com/',
                                             'http://139.9.213.120/')
        assert_that(datas).contains_key('api_host','app_key','share_icon','app_share_url','cm_qiniu_public','cm_qiniu_server','cm_normal_video_url','cm_secret_video_url')


if __name__ == '__main__':
    unittest.main()
