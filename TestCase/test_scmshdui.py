import time

from Common.baseui import baseUI


class Test_mshdui():
    def test_mshdui(self,driver):
        base =baseUI(driver)
        # 打开网址http://192.168.1.104:8090/#/login
        driver.get("http://192.168.1.104:8090/#/login")
        # 点击登录//span[contains(text(),'登录')]
        base.click("点击登录","//span[contains(text(),'登录')]")
        # 点击营销//span[contains(text(),'营销')]
        base.click("点击营销","//span[contains(text(),'营销')]")
        # 点击秒杀活动列表(//span[contains(text(),'秒杀活动列表')])[1]
        base.click("点击秒杀活动列表","(//span[contains(text(),'秒杀活动列表')])[1]")
        # 点击添加活动(//span[contains(text(),'添加活动')])[1]
        base.click("点击添加活动","(//span[contains(text(),'添加活动')])[1]")
        # 输入活动标题//div[@class='el-input el-input--small']/input
        base.send_keys("输入活动标题","//div[@class='el-input el-input--small']/input","test_秒杀2")
        # 输入开始时间(//input[@placeholder='请选择时间'])[1]
        base.send_keys("输入开始时间","(//input[@placeholder='请选择时间'])[1]","2019-06-01")
        # 输入结束时间(//input[@placeholder='请选择时间'])[2]
        base.send_keys("输入结束时间","(//input[@placeholder='请选择时间'])[2]","2019-06-09")
        # 点击确定//span[contains(text(),'确 定')]
        base.click("点击确定","//span[contains(text(),'确 定')]")
        # 确认点击确定//button[@class='el-button el-button--default el-button--small el-button--primary ']/span
        base.click("确认点击确定","//button[@class='el-button el-button--default el-button--small el-button--primary ']/span")
        time.sleep(2)


        # 输入筛选活动名称//input[@placeholder='活动名称']
        base.send_keys("点击筛选活动名称","//input[@placeholder='活动名称']","test_秒杀2")
        # 点击查询搜索//span[contains(text(),'查询搜索')]
        base.click("点击查询搜索","//span[contains(text(),'查询搜索')]")
        time.sleep(2)

        # 点击编辑(// span[contains(text(), '编辑')])[1]
        base.click("点击编辑","(// span[contains(text(), '编辑')])[1]")
        # 修改开始时间(//input[@placeholder='请选择时间'])[1]
        base.send_keys("修改开始时间","(//input[@placeholder='请选择时间'])[1]","2019-06-06")
        # 修改结束时间(//input[@placeholder='请选择时间'])[2]
        base.send_keys("修改结束时间","(//input[@placeholder='请选择时间'])[2]","2019-06-07")
        # 点击确定//span[contains(text(),'确 定')]
        base.click("点击确定","//span[contains(text(),'确 定')]")
        # 确认点击确定//button[@class='el-button el-button--default el-button--small el-button--primary ']/span
        base.click("确认点击确定","//button[@class='el-button el-button--default el-button--small el-button--primary ']/span")
        time.sleep(2)

        # 点击重置清空输入框//span[contains(text(),'重置')]
        base.click("点击重置清空输入框","//span[contains(text(),'重置')]")
        # 输入筛选活动名称//input[@placeholder='活动名称']
        base.send_keys("点击筛选活动名称","//input[@placeholder='活动名称']","test_秒杀2")
        # 点击查询搜索//span[contains(text(),'查询搜索')]
        base.click("点击查询搜索","//span[contains(text(),'查询搜索')]")
        time.sleep(2)


        # 点击删除(//span[contains(text(),'删除')])[1]
        base.click("点击删除","(//span[contains(text(),'删除')])[1]")
        # 点击确定//button[@class='el-button el-button--default el-button--small el-button--primary ']/span
        base.click("点击确定","//button[@class='el-button el-button--default el-button--small el-button--primary ']/span")
        time.sleep(2)

        # 点击重置清空输入框//span[contains(text(),'重置')]
        base.click("点击重置清空输入框","//span[contains(text(),'重置')]")
        # 输入筛选活动名称//input[@placeholder='活动名称']
        base.send_keys("点击筛选活动名称","//input[@placeholder='活动名称']","test_秒杀2")
        # 点击查询搜索//span[contains(text(),'查询搜索')]
        base.click("点击查询搜索","//span[contains(text(),'查询搜索')]")
        time.sleep(2)



