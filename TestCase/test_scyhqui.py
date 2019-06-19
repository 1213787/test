import time

from Common.baseui import baseUI

# 优惠券列表
class Test_scui():
    def test_scui1(self,driver):
        base=baseUI(driver)
        # 打开网址
        driver.get("http://192.168.1.104:8090")
        # 点击登录//span[contains(text(),'登录')]
        base.click("点击登录","//span[contains(text(),'登录')]")
        # 点击营销//span[contains(text(),'营销')]
        base.click("点击营销","//span[contains(text(),'营销')]")
        # 点击优惠券列表//span[contains(text(),'优惠券列表')]
        base.click("点击优惠券列表","//span[contains(text(),'优惠券列表')]")
        # 点击添加(//span[contains(text(),'添加')])[2]
        base.click("点击添加","(//span[contains(text(),'添加')])[2]")
        # 点击优惠券名称(//div[@class='input-width el-input el-input--small'])[1]/input
        base.send_keys("点击优惠券名称","(//div[@class='input-width el-input el-input--small'])[1]/input","哈哈哈哈")
        # 点击总发行量(//div[@class='input-width el-input el-input--small'])[2]/input
        base.send_keys("点击总发行量","(//div[@class='input-width el-input el-input--small'])[2]/input","1000")
        # 点击面额(//div[@class='input-width el-input el-input--small el-input-group el-input-group--append'])[1]/input
        base.send_keys("点击面额","(//div[@class='input-width el-input el-input--small el-input-group el-input-group--append'])[1]/input","200")
        # 点击使用门槛(//input[@placeholder='只能输入正整数'])[3]
        base.send_keys("点击使用门槛","(//input[@placeholder='只能输入正整数'])[3]","500")
        # 点击有效期(//input[@placeholder='选择日期'])[1]
        base.send_keys("点击有效期","(//input[@placeholder='选择日期'])[1]","2019-05-30")
        base.send_keys("点击有效期","(//input[@placeholder='选择日期'])[2]","2019-06-01")
        # 点击提交//span[contains(text(),'提交')]
        base.click("点击提交","//span[contains(text(),'提交')]")
        # 点击确认提交//button[@class='el-button el-button--default el-button--small el-button--primary ']
        base.click("点击确认提交","//button[@class='el-button el-button--default el-button--small el-button--primary ']")
        time.sleep(2)



        # 点击优惠券名称筛选搜索//input[@placeholder='优惠券名称']
        base.send_keys("点击优惠券名称筛选搜索","//input[@placeholder='优惠券名称']","哈哈哈哈")
        # 点击查询搜索//span[contains(text(),'查询搜索')]
        base.click("点击查询搜索","//span[contains(text(),'查询搜索')]")
        time.sleep(2)

        # 点击删除(//span[contains(text(),'删除')])[1]
        base.click("点击删除","(//span[contains(text(),'删除')])[1]")
        # 点击确定//span[contains(text(),'确定')]
        base.click("点击确定","//span[contains(text(),'确定')]")
        time.sleep(2)

        # 点击优惠券名称筛选搜索//input[@placeholder='优惠券名称']
        base.send_keys("点击优惠券名称筛选搜索","//input[@placeholder='优惠券名称']","哈哈哈哈")
        # 点击查询搜索//span[contains(text(),'查询搜索')]
        base.click("点击查询搜索","//span[contains(text(),'查询搜索')]")
        time.sleep(2)


        # 点击编辑(//span[contains(text(),'编辑')])[1]
        base.click("点击编辑","(//span[contains(text(),'编辑')])[1]")
        # 修改有效期(//input[@placeholder='选择日期'])[2]
        base.send_keys("修改有效期","(//input[@placeholder='选择日期'])[2]","2019-06-10")
        # 点击提交//span[contains(text(),'提交')]
        base.click("点击提交","//span[contains(text(),'提交')]")
        # 点击确认提交//button[@class='el-button el-button--default el-button--small el-button--primary ']
        base.click("点击确认提交","//button[@class='el-button el-button--default el-button--small el-button--primary ']")
        time.sleep(2)


        # 点击优惠券名称筛选搜索//input[@placeholder='优惠券名称']
        base.send_keys("点击优惠券名称筛选搜索","//input[@placeholder='优惠券名称']","哈哈哈哈")
        # 点击查询搜索//span[contains(text(),'查询搜索')]
        base.click("点击查询搜索","//span[contains(text(),'查询搜索')]")
        time.sleep(2)


