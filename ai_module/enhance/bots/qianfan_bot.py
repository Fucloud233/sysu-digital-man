# 填充API Key与Secret Key
import requests
import json

from enhance.bots.bot import Bot, BotType


class QianfanBot(Bot):
    def __init__(self):
        super().__init__(BotType.Qianfan)

    def _call_api(self, prompt: str):
        url = "https://aip.baidubce.com/oauth/2.0/token?client_id={}&client_secret={}&grant_type=client_credentials" \
            .format()
        
        payload = json.dumps("")
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        
        response = requests.request("POST", url, headers=headers, data=payload)
        
        return response.json().get("access_token")


def main():
        
    url = "https://aip.baidubce.com/oauth/2.0/token?client_id=【API Key】&client_secret=【Secret Key】&grant_type=client_credentials"
    
    payload = json.dumps("")
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    
    return response.json().get("access_token")
    

if __name__ == '__main__':
    access_token = main()
    print(access_token)
    