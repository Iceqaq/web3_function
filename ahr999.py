import httpx

def ahr999_index(url, days, index):
    client = httpx.Client()
    response = client.get(url)
    # 检查请求是否成功
    if response.status_code == 200:
        data = response.json()
        results = data['data']
        sum_values = 0.0
        count = 0
        for result in results[:days]:
            # 尝试将字符串转换为浮点数
            num = float(result[index])
            sum_values += num
            count += 1
        
        if count > 0:
            average = round(sum_values / count, 2)
            return average


def print_index_average(url, days, index, index_name):
    average = ahr999_index(url, days, index)
    if average is not None:
        result = (f"最近{days}天的{index_name}的平均值是: {average}")
        return (result)


def ahr999_get():
    url1 = 'https://api.deriexs.com/indicators/ahr999Hoarding'
    url2 = 'https://api.deriexs.com/indicators/ahr999Escape'
    results=[]
    #当前的ARH999指标
    results.append(print_index_average(url1, 1, 3, "AHR999屯币指数"))
    results.append(print_index_average(url2, 1, 2, "AHR999逃顶指数"))


    #最近5天的屯币指数和逃顶指数
    results.append(print_index_average(url1, 5, 3, "AHR999屯币指数"))
    results.append(print_index_average(url2, 5, 2, "AHR999逃顶指数"))

    # 获取最近20天的屯币指数和逃顶指数
    results.append(print_index_average(url1, 20, 3, "AHR999屯币指数"))
    results.append(print_index_average(url2, 20, 2, "AHR999逃顶指数"))
    # 获取最近25天的屯币指数和逃顶指数
    results.append(print_index_average(url1, 25, 3, "AHR999屯币指数"))
    results.append(print_index_average(url2, 25, 2, "AHR999逃顶指数"))
    # 获取最近30天的屯币指数和逃顶指数
    results.append(print_index_average(url1, 30, 3, "AHR999屯币指数"))
    results.append(print_index_average(url2, 30, 2, "AHR999逃顶指数"))


    # 获取最近90天的屯币指数和逃顶指数
    results.append(print_index_average(url1, 90, 3, "AHR999屯币指数"))
    results.append(print_index_average(url2, 90, 2, "AHR999逃顶指数"))

    # 获取最近180天的屯币指数和逃顶指数
    results.append(print_index_average(url1, 180, 3, "AHR999屯币指数"))
    results.append(print_index_average(url2, 180, 2, "AHR999逃顶指数"))

    return results


