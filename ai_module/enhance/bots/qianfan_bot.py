# 填充API Key与Secret Key
import requests
import json
from enum import IntEnum

from config import CONFIG
from bots.bot import Bot
from bots.type import BotType

class QianfanModelType(IntEnum):
    ERNIE_Bot_turbo = 0
    ERNIE_Bot_4 = 1

# 

class QianfanBot(Bot):
    def __init__(self):
        super().__init__(BotType.Qianfan)
        # TODO: 需要对这里进行异常处理
        self.__access_token = self.__get_access_token()
        self.__model_type = QianfanModelType.ERNIE_Bot_4
        # self.__model_type = QianfanModelType.ERNIE_Bot_turbo

    def _call_api(self, prompt: str):
        payload = json.dumps({
            "messages": [
                {
                    "role": "user", "content": self.sys_prompt + '\n' + prompt,
                    
                }# "role": "user", "content": prompt
            ]
        })
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", self.__get_request_url(self.__model_type), headers=headers, data=payload)

        try:
            return response.json()['result']
        except KeyError:
            print(response.text)
 
    def __get_access_token(self):
        payload = json.dumps("")
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        
        response = requests.request("POST", self.__get_auth_url(), headers=headers, data=payload)
        return response.json().get("access_token")
           
    def __get_auth_url(self):
        (api_key, api_secret) = CONFIG.api_key(self.type)
        return "https://aip.baidubce.com/oauth/2.0/token?client_id={}&client_secret={}&grant_type=client_credentials" \
            .format(api_key, api_secret)
    
    def __get_request_url(self, model_type: QianfanModelType):
        url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/"

        if model_type == QianfanModelType.ERNIE_Bot_turbo:
            url += "eb-instant"
        elif model_type == QianfanModelType.ERNIE_Bot_4:
            url += "completions_pro"
        
        return url + "?access_token={}".format(self.__access_token)
    