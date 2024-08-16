import httpx
import json


def fetch_jinse_lives(limit=20, category=1):
    # 定义请求的 URL 和头部信息
    url = "https://api.jinse.cn/noah/v2/lives"
    headers = {
        "Host": "api.jinse.cn",
        "X-Jinse-Signature": "",
        "Sec-Ch-Ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        "Source": "web",
        "X-Jinse-Api-Version": "v1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
        "Sec-Ch-Ua-Mobile": "?0",
        "Accept": "application/json, text/plain, */*",
        "Token": "undefined",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Origin": "https://www.jinse.cn",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://www.jinse.cn/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Priority": "u=1, i",
        "Connection": "keep-alive"
    }

    # 定义请求参数
    params = {
        "limit": str(limit),
        "reading": "false",
        "source": "web",
        "flag": "down",
        "id": "0",
        "category": str(category)
    }

    # 发送 GET 请求
    response = httpx.get(url, headers=headers, params=params)

    # 检查响应状态码
    if response.status_code == 200:
        results=[]
        # 解析 JSON 数据
        data = response.json()
        # 获取 list 数组
        if "list" in data:
            list_data = data["list"]
            # 打印 list 数组
            for data in list_data:
                date = data['date']
                lives = data['lives']
                for live in lives:
                    
                    Id = live.get('id')
                    Content = live.get('content')
                    up_counts = live.get('up_counts')
                    down_counts = live.get('down_counts')
                    result=(f'{Id},{date}, {Content}, 利多支持数{up_counts}, 利空支持数{down_counts}')
                    results.append(result)
    return results


