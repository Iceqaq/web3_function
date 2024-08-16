import httpx
import numpy as np
from scipy import stats

def determine_trend(data):
    # 创建特征矩阵（X）和目标向量（y）
    X = np.arange(len(data)).reshape(-1, 1)
    y = np.array(data).reshape(-1, 1)

    # 使用线性回归计算斜率
    slope, _, _, _, _ = stats.linregress(X.flatten(), y.flatten())

    # 根据斜率判断趋势
    if slope < 0:
        return "上升趋势"
    elif slope > 0:
        return "下降趋势"
    else:
        return "无明显趋势"

# 使用 httpx 发送 GET 请求并获取响应
def fetch_data(coin,time):
    # 大户账户数多空比
    url1 = f'https://fapi.binance.com/futures/data/topLongShortAccountRatio?symbol={coin}&period={time}'

    # 大户持仓量多空比
    url2 = f'https://fapi.binance.com/futures/data/topLongShortPositionRatio?symbol={coin}&period={time}'

    # 多空持仓人数比
    url3 = f'https://fapi.binance.com/futures/data/globalLongShortAccountRatio?symbol={coin}&period={time}'

    urls = [url1, url2, url3]
    results = []
    for url in urls:
        response = httpx.get(url)
        if response.status_code == 200:
            results.append(response.json())
        else:
            raise Exception(f"Failed to fetch data from {url}, status code: {response.status_code}")
    
    return results

def binance_get(coins,time):
    binance_result=[]
    for coin in coins:
        data = fetch_data(coin,time)
        A = data[0]  # 大户账户数多空比
        B = data[1]  # 大户持仓量多空比
        C = data[2]  # 多空持仓人数比

        resultsA = []
        resultsB = []
        resultsC = []

        for aa, bb, cc in zip(A, B, C):
            resultsA.append(float(aa['longAccount']))
            resultsB.append(float(bb['longAccount']))
            resultsC.append(float(cc['longAccount']))

        trendA = determine_trend(resultsA)
        trendB = determine_trend(resultsB)
        trendC = determine_trend(resultsC)

        AA=(f"以{time} 为单位 {coin} 大户账户数多空比趋势: {trendA},数据为{resultsA}")
        BB=(f"以{time} 为单位 {coin} 大户持仓量多空比趋势: {trendB}，数据为{resultsB}")
        CC=(f"以{time} 为单位 {coin} 多空持仓人数比趋势: {trendC}，数据为{resultsC}")
        binance_result.append(AA)
        binance_result.append(BB)
        binance_result.append(CC)

    return binance_result