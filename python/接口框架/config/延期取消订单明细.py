import requests
class dingdan(object):
    def mx(self):
        url = "https://mobileqa.dms.saic-gm.com/api/sit/pol4s/pol4sPartOrder/rest/pol4s/delayOrderCancelStatus/getCancelDelayOrder"

        payload = "{\r\n \"pageNum\": 3,\r\n \"pageSize\": 1,\r\n \"queryTerms\": {\r\n    \"orderNo\":\"R2100654\",\r\n    \"cancelStatus\":-1,\r\n    \"applyStartDate\":20180801,\r\n    \"applyEndDate\":20180909\r\n }\r\n}"
        headers = {
            'Content-Type': "application/json",
            'x-dealer-code': "2100001",
            'x-position-code': "D_PO_1028",
            'x-resource-code': "pol4s_delayOrderCancelStatus_getCancelDelayOrder",
            'x-track-code': "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
            'x-user-code': "dhxc1u",
            'x-access-token': "8405e48dd499a8a329afe8e8d8e7da3b",
            'User-Agent': "PostmanRuntime/7.15.0",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Postman-Token': "bc608458-19b3-4f21-a16c-ef0c929db502,f9a01061-c381-4fc3-a686-68b218c7102e",
            'Host': "mobileqa.dms.saic-gm.com",
            'cookie': "dapp.sgm.com:qa:=8405e48dd499a8a329afe8e8d8e7da3b; dapp.sgm.com:qa:=8405e48dd499a8a329afe8e8d8e7da3b; fdaa0f2d854071f7f82d1c80a99830bb=2d45a497bf053a6a9a23955ddef3f0bd; a689baa2b7060531c4d0be5b10aa7055=a3a54f569b14d5196ef24d5b4b890058",
            'accept-encoding': "gzip, deflate",
            'content-length': "171",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
            }

        response = requests.request("POST", url, data=payload, headers=headers)
        return response.json()
if __name__ == '__main__':
    print(dingdan().mx())