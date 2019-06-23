import requests
# import sys
# sys.path.append(r'E:\python\接口框架')
from 接口框架.data.dingdan_duqu import shuju
class dingdan(object):
    def chaming(self,num):
        url = "https://mobileqa.dms.saic-gm.com/api/sit/pol4s/pol4sPartOrder/rest/pol4s/partOrderSearch/partOrderDetailSearch"
        header= {
    'Content-Type': "application/json",
    'x-dealer-code': "2100005",
    'x-position-code': "D_PO_1028",
    'x-resource-code': "pol4s_partOrderSearch_partOrderDetailSearch",
    'x-track-code': "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
    'x-user-code': "dhxc1u",
    'token': "3561c0b9bc2c9391c4f439c694a8ee79",
    'User-Agent': "PostmanRuntime/7.15.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "367751ea-eac3-4fe3-bafe-b2061895d7eb,23368008-1211-461b-bd14-d0d581fbac67",
    'Host': "mobileqa.dms.saic-gm.com",
    'cookie': "dapp.sgm.com:qa:=c909d3541a63a46b75f314a4e94828c0; dapp.sgm.com:qa:=c909d3541a63a46b75f314a4e94828c0; fdaa0f2d854071f7f82d1c80a99830bb=2d45a497bf053a6a9a23955ddef3f0bd; a689baa2b7060531c4d0be5b10aa7055=b1100f0adf89b706031ddd7ab44c593f",
    'accept-encoding': "gzip, deflate",
    'content-length': "96",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }
        pyloa="{\r\n \"pageNum\":\"%d\",\r\n \"pgeSize\":\"10\",\r\n \"queryTerms\":\r\n {\r\n  \"orderNo\":\"V2100880181219390\"\r\n }\r\n}" % (num)

        response = requests.request("POST", url, data=pyloa, headers=header)
        return response.json()
if __name__ == '__main__':
   for i in shuju():
       # print(i)
        print(dingdan().chaming(i[0]))