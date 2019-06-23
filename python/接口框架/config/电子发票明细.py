import requests
class dzfp(object):
    def mx(self):
        url = "https://mobileqa.dms.saic-gm.com/api/sit/pol4s/pol4sPartOrder/rest/pol4s/partOrder/electricInvoiceDetail"

        payload = "{\r\n  \"pageNum\": 1,\r\n  \"pageSize\": 10,\r\n  \"queryTerms\":\r\n  {\r\n  \t\"billingNo\":\"0914222771\"\r\n  }\r\n}"
        headers = {
            'Content-Type': "application/json",
            'x-dealer-code': "2100001",
            'x-position-code': "D_PO_1028",
            'x-resource-code': "pol4s_partOrder_electricInvoiceDetail",
            'x-track-code': "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
            'x-user-code': "dhxc1u",
            'x-access-token': "8405e48dd499a8a329afe8e8d8e7da3b",
            'User-Agent': "PostmanRuntime/7.15.0",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Postman-Token': "6e9e1542-1863-4b76-99bf-bfce4634eccc,7f1aef35-d820-4ec9-aec4-b430c2293d4d",
            'Host': "mobileqa.dms.saic-gm.com",
            'cookie': "dapp.sgm.com:qa:=8405e48dd499a8a329afe8e8d8e7da3b; dapp.sgm.com:qa:=8405e48dd499a8a329afe8e8d8e7da3b; fdaa0f2d854071f7f82d1c80a99830bb=2d45a497bf053a6a9a23955ddef3f0bd; a689baa2b7060531c4d0be5b10aa7055=a3a54f569b14d5196ef24d5b4b890058",
            'accept-encoding': "gzip, deflate",
            'content-length': "96",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }

        response = requests.request("POST", url, data=payload, headers=headers)
        return response.json()
if __name__ == '__main__':
    print(dzfp().mx())