import requests
import json

def website_dingtalk(title,contents):
    # 测试webhook
    ding_url = "https://oapi.dingtalk.com/robot/send?access_token=b8c41d432090393c45cdf5f066b6c0ad28811e067c6973c721d4309015e62ef6"

    
    headers = {'Content-Type': 'application/json'}
    payload={
        "msgtype": "actionCard",
        "actionCard": {
            "title": title,
            "text": f'''#### {title}\n\n
                        \n\n
                        {contents}\n\n
                        \n\n
                        ''',
        }
    }

    response = requests.post(ding_url, headers=headers, data=json.dumps(payload))

    
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print("Failed to send message.")


