import requests
import json

def coincap_get(coin,time, directions):
    #https://api.coincap.io/v2/assets 获取coin_id
    url = f"https://api.coincap.io/v2/assets/{coin}/history?interval={time}"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    # 检查响应状态码
    if response.status_code == 200:
        # 解析 JSON 数据
        data = response.json()
        
        # 提取 data 字段
        history_data = data.get('data', [])
        
        # 确保 history_data 至少有 30 条数据
        if len(history_data) >= 30:
            # 初始化累加器
            sum_1 = 0
            sum_5 = 0
            sum_15 = 0
            sum_30 = 0
            
            # 遍历最后 30 条数据
            for i in range(1, 31):
                price_usd = float(history_data[-i].get('priceUsd'))
                if i <= 1:
                    sum_1 += price_usd
                if i <= 5:
                    sum_5 += price_usd
                if i <= 15:
                    sum_15 += price_usd
                sum_30 += price_usd
            
            # 计算平均值
            avg_1 = sum_1 / 1
            avg_5 = sum_5 / 5
            avg_15 = sum_15 / 15
            avg_30 = sum_30 / 30
            
            # 返回平均值的字典
            return {
                'coin':coin,
                "directions": directions,
                "time": time,
                "avg_1": avg_1,
                "avg_5": avg_5,
                "avg_15": avg_15,
                "avg_30": avg_30
            }
        else:
            return {"error": "Not enough data to calculate averages."}
    else:
        return {"error": f"Failed to retrieve data, status code: {response.status_code}"}


def sum_coincap(coin):
# 调用函数并处理返回值
    results = []
    results.append(coincap_get(coin,'m1', '现在的价格'))
    results.append(coincap_get(coin,'m15', '以15分钟为单位'))
    results.append(coincap_get(coin,'h1', '以1小时为单位'))
    results.append(coincap_get(coin,'h2', '以2小时为单位'))
    results.append(coincap_get(coin,'h6', '以6小时为单位'))
    
    # 打印结果
    return results