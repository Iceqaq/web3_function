import httpx
import json
from datetime import datetime

# 获取当前时间
now = datetime.now()
formatted_time = now.strftime('%Y-%m-%d %H:%M:%S')
def bi123():
    url = "https://www.bi123.co/crypto-web/open/signal/list"
    headers = {
        "Host": "www.bi123.co",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "Sec-Ch-Ua": "\"Not)A;Brand\";v=\"99\", \"Google Chrome\";v=\"127\", \"Chromium\";v=\"127\"",
        "Locale": "zh-CN",
        "Sec-Ch-Ua-Mobile": "?0",
        "Authorization": "",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
        "Content-Type": "application/json;charset=UTF-8",
        "Accept": "application/json",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Origin": "https://www.bi123.co",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://www.bi123.co/signal/trendfollowing",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Priority": "u=1, i",
        "Connection": "keep-alive"
    }
    # 定义请求体
    data = {
        "type": 0,
        "current": 1,
        "size": 10,
        "isUp": "",
        "wellChosen": "",
        "duration": "4H",
        "contract": "BTC/USDT",
        "sortName": "",
        "sortOrder": "",
        "isFundingRate": "",
        "isLong": "",
        "openInterestDivTotalSupply": "",
        "isClose": ""
    }

    # 发送 POST 请求
    response = httpx.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        # 解析 JSON 响应
        response_data = response.json()
        Trend_tracking=response_data['data']['records']
        signer=(Trend_tracking[0]['signer'])
        price=(Trend_tracking[0]['price'])
        time=(Trend_tracking[0]['time'])
        result={
            'time':time,
            'signer':signer,
            'price':price,
            'priceChangePercent':'priceChangePercent'
        }
        return  result
    else:
        print(f"Request failed with status code {response.status_code}")

def bi123_get():
    bi123_result=bi123()
    if (formatted_time)==bi123_result['time']:
        result=f'这是趋势追踪，参数如下{bi123_result}'
        return result
    else:
        return None 