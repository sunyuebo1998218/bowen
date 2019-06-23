import requests
class yqcx(object):
    def cx(self):
        url = "https://mobileqa.dms.saic-gm.com/api/sit/pol4s/pol4sPartOrder/rest/pol4s/delayOrderCancelStatus/getCancelDelayOrder"

        payload = "{\n    \"pageNum\": 3,\n    \"pageSize\": 1,\n    \"queryTerms\": {\n        \"orderNo\": \"R2100654\",\n        \"cancelStatus\": -1,\n        \"applyStartDate\": 20180801,\n        \"applyEndDate\": 20180909\n    }\n}"
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
            'Postman-Token': "aef1b86a-8d7c-46d1-aa0c-2a9205854ecf,953f89b5-f296-4c0f-b63d-a0ad8be924de",
            'Host': "mobileqa.dms.saic-gm.com",
            'cookie': "dapp.sgm.com:qa:=8405e48dd499a8a329afe8e8d8e7da3b; dapp.sgm.com:qa:=8405e48dd499a8a329afe8e8d8e7da3b; fdaa0f2d854071f7f82d1c80a99830bb=2d45a497bf053a6a9a23955ddef3f0bd; a689baa2b7060531c4d0be5b10aa7055=b1100f0adf89b706031ddd7ab44c593f",
            'accept-encoding': "gzip, deflate",
            'content-length': "171",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        return response.json()
if __name__ == '__main__':
    print(yqcx().cx())