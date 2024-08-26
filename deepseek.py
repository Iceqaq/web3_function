# -*- coding: utf-8 -*-

# python3
# Please install OpenAI SDK first: `pip3 install openai`
from openai import OpenAI

class ChatBot:
    def __init__(self,model="deepseek-chat", 
                 prompt='''你现在是一个精通金融的币圈交易分析师,请帮我以专业的视角和方法提出当下的建议,请认真分析,不允许乱编,乱说,不允许以任意理由拒绝回答,需要一次性回答完毕,尽可能不要废话
                 接下来我会传入一些内容,这是一个字典,请帮我进行分析,请全面的结合各类观点
                    1、最近最新20条相关币圈相关资讯,键值为jinse_results,来源为金色财经,这是一个专业的币圈咨询网站
                    2、最近最新20条相关币圈相关资讯,键值为theblockbeats_results,来源于律动BLOCKBEATS,这一个专业的币圈咨询网站
                    3、最近的某个币的价格,分别以1分钟,5分钟,1小时,2小时,6小时作为单位,并且以1分钟作为当前的价格,其他是以5,15,30个单位的平均值,键值为price_results
                    4、持多仓的大户、账户比率,键值为binance_results
                    5、这个是某专业的网站对现在的趋势判断,键值为bi123_results,请注意，该值不是任何时间都有，如果没有请无视，如果有请判断
                    6、利用arh999的指标来判断BTC的币价是贵还是便宜,键值ahr999_results,请注意：如果是震荡期间该指标才准确,如果非震荡期间该指标则失效
                    最后、上面的键值里可能有多种币的种类,例如price_results,请不要只分析一种

                我想获取的结果是判断该该加密后货币未来一阵子最有可能的趋势,返回内容格式可以参考如下：
                    1、币种名称,及现在的价格
                    2、从资讯里获取市场情绪,判断短期的趋势
                    3、从最近的5m,1h,2h均价里,判断短期的趋势
                    4、从最近的6h均价里,判断中期的趋势
                    5、从大户多空比来看,判断短期的趋势
                    6、bi123_results是趋势判断,结合之前的数据，判断该结论是否正确
                    7、通过ahr999_results来分析,如果最近1天
                    最后、给出对当前情况的判断,做空，做多,暂不交易,并最好给出止盈止损位置
                    要求输出的格式有正确的高亮，能一眼看到关键

                 '''):
        self.client = OpenAI(api_key='sk-134c25c6dbb04431af28b996bb5ed723', base_url='https://api.deepseek.com')
        self.model = model
        self.prompt = prompt


    def get_response(self, content):
        messages = [
            {"role": "system", "content": self.prompt},
            {"role": "user", "content": content}
        ]
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            stream=False
        )
        
        return response.choices[0].message.content

