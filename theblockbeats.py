import requests
import time


def theblockbeats_get():
# 定义请求的URL和头部信息
    url = "https://api.theblockbeats.info/v2/newsflash/list"
    headers = {
        "Host": "api.theblockbeats.info",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate, br",
        "Lang": "cn",
        "Origin": "https://www.theblockbeats.info",
        "Referer": "https://www.theblockbeats.info/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "Priority": "u=0",
        "Te": "trailers",
        "Connection": "keep-alive"
    }

    # 定义请求的参数
    params = {
        "page": 1,
        "limit": 20,
        "ios": 1,
        "end_time": "",
        "detective": 1
    }

    # 发送GET请求
    response = requests.get(url, headers=headers, params=params)

    # 检查响应状态码
    if response.status_code == 200:
        # 解析JSON响应
        data = response.json()
        datas = data['data']['list']

        # 处理数据
        results = []
        for i in datas:
            timestamp = i['add_time']
            time_struct = time.localtime(timestamp)
            formatted_date = time.strftime("%Y-%m-%d", time_struct)
            content = i['content']
            results.append({
                "time": formatted_date,
                "content": content
            })

        return results

