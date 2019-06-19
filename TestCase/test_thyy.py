from Common import Request, Assert, read_excel, Login
import allure
import pytest
request = Request.Request()
assertion = Assert.Assertions()
idsList=[]
excel_list = read_excel.read_excel_list('../document/th.xlsx')
length = len(excel_list)
for i in range(length):
    idsList.append(excel_list[i].pop())
url = 'http://192.168.1.137:8080/'
head = {}
item_id=0
@allure.feature('退订')
class Test_th:

    @allure.story('查询列表')
    def test_th_list(self):
        global head
        head = Login.Login().get_token()
        th_list_resp = request.get_request(url=url + 'returnReason/list', params={'pageNum': 1, 'pageSize': 5}, headers=head)
        resp_json = th_list_resp.json()
        json_data = resp_json['data']
        data_list = json_data['list']
        item = data_list[0]
        global item_id
        item_id = item['id']
        assertion.assert_code(th_list_resp.status_code, 200)
        assertion.assert_in_text(resp_json['message'], '成功')

    @allure.story('删除')
    def test_del_th(self):
        del_resp = request.post_request(url=url + 'returnReason/delete/', params={'ids':item_id}, headers=head)
        resp_json = del_resp.json()
        assertion.assert_code(del_resp.status_code, 200)
        assertion.assert_in_text(resp_json['message'], '成功')

    @allure.story("添加")
    @pytest.mark.parametrize("name,sort,msg", excel_list, ids=idsList)
    def test_add_th(self,name,sort,msg):
        req_json = {"name":name,"sort":sort,"status":1,"createTime":""}
        add_th_resp = request.post_request(url=url + 'returnReason/create', json=req_json, headers=head)
        resp_json = add_th_resp.json()
        assertion.assert_code(add_th_resp.status_code, 200)
        assertion.assert_in_text(resp_json['message'],msg)
