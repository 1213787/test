from Common import Request, Assert
import allure
import pytest

request = Request.Request()
assertion = Assert.Assertions()

url = 'http://192.168.1.137:1811/'
head = {}


@allure.feature('用户模块')
class Test_yhmk:

    @allure.story('注册')
    def test_zc_list(self):

        post_request = request.post_request(url=url + '/user/signup',
                                            json={"phone": "18877897895", "pwd": "ttt123456", "rePwd": "ttt123456",
                                                  "userName": "ttt123456"})
        resp_dict = post_request.json()
        print(type(resp_dict))

        assertion.assert_code(post_request.status_code, 200)
        assertion.assert_in_text(resp_dict['respBase'], '成功')
