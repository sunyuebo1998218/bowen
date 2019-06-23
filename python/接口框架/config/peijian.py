import requests
# import sys
# sys.path.append(r'E:\python\接口框架')
from 接口框架.data.dingdan_duqu import shuju
class Ding_Dan(object):
    def cha_mingxi(self,num):
        url = "https://mobileqa.dms.saic-gm.com/api/sit/pol4s/pol4sPartOrder/rest/pol4s/partOrder/orderPartDetail"
        header= {
              'Content-Type': "application/json",
    'x-dealer-code': "2100001",
    'x-position-code': "D_PO_1028",
    'x-resource-code': "pol4s_partOrder_orderPartDetail",
    'x-track-code': "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
    'x-user-code': "dhxc1u",
    'x-access-token': "c909d3541a63a46b75f314a4e94828c0",
    'User-Agent': "PostmanRuntime/7.15.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "475a7e3d-0269-4518-96f9-cfd445a80a56,12cc19e7-8f1b-42d6-8b3c-57c69649f385",
    'Host': "mobileqa.dms.saic-gm.com",
    'cookie': "dapp.sgm.com:qa:=54c7fe1fa7fa7f627c7720e0249e0f36; dapp.sgm.com:qa:=54c7fe1fa7fa7f627c7720e0249e0f36; fdaa0f2d854071f7f82d1c80a99830bb=2d45a497bf053a6a9a23955ddef3f0bd; a689baa2b7060531c4d0be5b10aa7055=b1100f0adf89b706031ddd7ab44c593f",
    'accept-encoding': "gzip, deflate",
    'content-length': "32",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }
        pyloa="{\r\n \"partOrderItemId\": %d\r\n}" % (num)

        response = requests.request("POST", url, data=pyloa, headers=header)
        return response.json()
if __name__ == '__main__':
   for i in shuju():
        print(Ding_Dan().cha_mingxi(i[0]))