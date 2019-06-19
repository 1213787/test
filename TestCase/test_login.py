# import time
#
# from Common import Request, Assert, read_excel
# import allure
# import pytest
#
# from Common.baseui import baseUI
#
# request = Request.Request()
# assertion = Assert.Assertions()
# idsList=[]
# excel_list = read_excel.read_excel_list('./document/test.xlsx')
# length = len(excel_list)
# for i in range(length):
#     idsList.append(excel_list[i].pop())

#
# url = 'http://192.168.1.137:8080/'
# head = {}
#
#
# @allure.feature("登录功能")
# class Test_login:
#
#      @allure.story("登录")
#      def test_login(self):
#         # =后面 :  request对象 调用了  post_request  方法,传入了两个参数
#         # = 前面:  将方法 返回的 对象/变量  起一个名字
#         login_resp = request.post_request(url=url+'admin/login',json={"username": "admin", "password": "123456"})
#
#
#         # 响应 . text  :  就是获取 text属性的内容,这个就是 响应正文 (str 格式)
#         resp_text = login_resp.text
#         print(type(resp_text))
#
#         # 响应 .json()  :  就是获取 字典格式的内容,这个就是 响应正文 (字典 格式)
#         resp_dict = login_resp.json()
#         print(type(resp_dict))
#
#         # .assert_code 用来断言 状态码 第一个参数填响应的状态码 第二个参数期望值
#         assertion.assert_code(login_resp.status_code,200)
#         # .assert_in_text 用来断言字符 第一个参数填 比较多的那个字符 第二个参数填这个字符 是否存在第一个里面
#         assertion.assert_in_text(resp_dict['message'],'成功')
#
#         data_dict = resp_dict['data']
#         token = data_dict['token']
#         tokenHead = data_dict['tokenHead']
#         global head
#         head ={'Authorization' : tokenHead+token}
#
#
#      @allure.story("获取用户信息")
#      def test_info(self):
#         # =后面 :  request对象 调用了  get_request  方法,传入了两个参数
#         # = 前面:  将方法 返回的 对象/变量  起一个名字
#         info_resp = request.get_request(url=url+ 'admin/info', headers=head)
#
#         # 响应 .json()  :  就是获取 字典格式的内容,这个就是 响应正文 (字典 格式)
#         resp_dict = info_resp.json()
#
#
#         assertion.assert_code(info_resp.status_code, 200)
#         assertion.assert_in_text(resp_dict['message'], '成功')
#
#
#
#
#
#
#      @allure.story("测试登录")
#      @pytest.mark.parametrize("username,password,msg",
#                               [['admin', '123456', '成功'], ['admin1', '123456', '错误'], ['admin', '123456a', '错误'],
#                                ['admin', '123456', '成功'], ['admin1', '123456', '错误'], ['admin', '123456a', '错误']],
#                               ids=['登录成功', '用户名错误', '密码错误', '登录成功1', '用户名错误1', '密码错误1']
#                               )
#      def test_login1(self, username, password, msg):
#          # =后面 :  request对象 调用了  post_request  方法,传入了两个参数
#          # = 前面:  将方法 返回的 对象/变量  起一个名字
#          login_resp = request.post_request(url=url + 'admin/login',
#                                            json={"username": username, "password": password})
#
#          # 响应 . text  :  就是获取 text属性的内容,这个就是 响应正文 (str 格式)
#          resp_text = login_resp.text
#          print(type(resp_text))
#
#          # 响应 .json()  :  就是获取 字典格式的内容,这个就是 响应正文 (字典 格式)
#          resp_dict = login_resp.json()
#
#          print(type(resp_dict))
#
#          # .assert_code 用来断言 状态码 ; 第一个参数 填 响应的状态码, 第二个参数 期望值
#          assertion.assert_code(login_resp.status_code, 200)
#
#          # .assert_in_text 用来断言字符 第一个参数填 比较多的那个字符; 第二参数填 这个字符 是否存在第一个字符里面
#          assertion.assert_in_text(resp_dict['message'], msg)
#
#
#
#
#
#
#
#
#
#      @allure.story("测试登录2")
#      @pytest.mark.parametrize("username,password,msg",excel_list,ids=idsList)
#      def test_login2(self, username, password, msg):
#         # =后面 :  request对象 调用了  post_request  方法,传入了两个参数
#         # = 前面:  将方法 返回的 对象/变量  起一个名字
#         login_resp = request.post_request(url=url + 'admin/login',
#                                           json={"username": username, "password": password})
#
#         # 响应 . text  :  就是获取 text属性的内容,这个就是 响应正文 (str 格式)
#         resp_text = login_resp.text
#         print(type(resp_text))
#
#         # 响应 .json()  :  就是获取 字典格式的内容,这个就是 响应正文 (字典 格式)
#         resp_dict = login_resp.json()
#
#         print(type(resp_dict))
#
#         # .assert_code 用来断言 状态码 ; 第一个参数 填 响应的状态码, 第二个参数 期望值
#         assertion.assert_code(login_resp.status_code, 200)
#
#         # .assert_in_text 用来断言字符 第一个参数填 比较多的那个字符; 第二参数填 这个字符 是否存在第一个字符里面
#         assertion.assert_in_text(resp_dict['message'], msg)
#
#
#
import time

from Common.baseui import baseUI


class Test_login():
    def test_login(self, driver):
        base=baseUI(driver)
        driver.get("http://192.168.1.128:8090/#/login")
        # 输入用户名//input[@name="username"]
        # base.send_keys('输入用户名',"//input[@name='username']","admin")
        # 密码输入框("//input[@name='password']")
        # base.send_keys('输入密码',"//input[@name='password']","123456")
        #点击登录按钮(//span[contains(text(),'登录')])[1]
        base.click('点击登录按钮',"(//span[contains(text(),'登录')])[1]")
        print(driver.page_source)
        assert "首页" in driver.page_source
        time.sleep(2)

        #点击订单(//span[contains(text(),'订单')])[1]
        base.click('点击订单',"(//span[contains(text(),'订单')])[1]")
        #点击订单列表//span[contains(text(),'订单列表')]
        base.click('点击订单列表',"//span[contains(text(),'订单列表')]")
        #订单状态选择待发货(//input[@placeholder="全部"])[1]
        base.click("订单状态","(//input[@placeholder='全部'])[1]")
        base.click("点击待发货","//span[contains(text(),'待发货')]")
        #点击查询搜索//span[contains(text(),'查询搜索')]
        base.click("点击查询搜索","//span[contains(text(),'查询搜索')]")
        #选择第一条订单，点击订单发货(//span[contains(text(),'订单发货')])[1]
        base.click("点击订单发货","(//span[contains(text(),'订单发货')])[1]")
        #选择配送方式//div[contains(text(),'配送方式')]
        base.click("配送方式","//div[contains(text(),'配送方式')]")
        base.click("点击选择物流公司","//input[@placeholder='请选择物流公司']")
        base.click("选择顺丰快递","//span[contains(text(),'顺丰快递')]")
        #输入物流单号(//input[@class='el-input__inner'])[2]
        base.send_keys("输入物流单号","(//input[@class='el-input__inner'])[2]","123456789")
        #点击确定//span[contains(text(),'确定')]
        base.click("点击确定","//span[contains(text(),'确定')]")
        #点击确认提示//button[@class='el-button el-button--default el-button--small el-button--primary ']
        base.click("点击确认提示","//button[@class='el-button el-button--default el-button--small el-button--primary ']")
        #获取提示文本并断言
        print(driver.page_source)
        assert "数据列表" in driver.page_source






