"""
------------------------------------
@Time : 2019/6/1 14:21
@Auth : linux超
@File : test_Recharge_api.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
------------------------------------
"""
from common.SendRequests import request
from common.ParseConfig import do_conf

# 登录


class LoginApi(object):
    request = request

    def login_api(self, method, url, data):
        self.request(method=method,
                     url=url,
                     data=data
                     )

    def close(self):
        self.request.close_session()


login = LoginApi()


if __name__ == '__main__':
    login = LoginApi()
    login.login_api(method='post',
                    url=do_conf('URL', 'Host_Url')+'/member/login',
                    data={"mobilephone": "18987560249", "pwd": "123457"})
    login.request.close_session()
