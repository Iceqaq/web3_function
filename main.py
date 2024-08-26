from deepseek import ChatBot
import coincap
import jinse
import theblockbeats
import ding_talk
import binance
import bi123
import ahr999
from datetime import datetime

def content_sum():
    #bi123  趋势获取
    bi123_results = bi123.bi123_get()

    #咨询信息
    jinse_results = jinse.fetch_jinse_lives()
    theblockbeats_results = theblockbeats.theblockbeats_get()

    #ahr999指标
    ahr999_results = ahr999.ahr999_get()

    # 价格
    price_results = []
    coins = ['bitcoin', 'ethereum','solana','dogecoin']
    for coin in coins:
        results = coincap.sum_coincap(coin)
        for result in results:
            if "error" in result:
                print(result["error"])
            else:
                price_results.append(f'''币种类型:{result['coin']} :{result['directions']} :Average price of last 1 price with: 
                                     最新的价格{result['avg_1']},
                                     最新的5次平均价格{result['avg_5']},
                                     最新的15次平均价格{result['avg_15']},
                                     最新的30次平均价格{result['avg_30']}''')
                print(f'''币种类型 :{result['coin']} :{result['directions']} :Average price of last 1 price with: 
                                     最新的价格{result['avg_1']},
                                     最新的5次平均价格{result['avg_5']},
                                     最新的15次平均价格{result['avg_15']},
                                     最新的30次平均价格{result['avg_30']}''')
                
    #币安持仓比
    b_coins = ['BTCUSDT', 'ETHUSDT','SOLUSDT','DOGEUSDT']
    b_times = '15m'
    binance_results = binance.binance_get(b_coins, b_times)

    content = {'jinse_results': jinse_results,
               'theblockbeats_results': theblockbeats_results,
               'price_results': price_results,
               'binance_results': binance_results,
               'bi123_results': bi123_results,
               'ahr999_results': ahr999_results,
               }

    return content

if __name__ == "__main__":
    now = datetime.now()
    if now.hour>8:
        print(now.hour)
        content = content_sum()
        print(content)
        chatbot = ChatBot()
        response = chatbot.get_response(str(content))
        print('\r\n')
        print('----------------------response----------------------')
        print(response)
        ding_talk.website_dingtalk('币圈监控', response)
    else:
        print("当前时间不在允许的执行范围内，程序将不会执行。")