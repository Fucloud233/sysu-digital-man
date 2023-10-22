# import json
import sys
sys.path.append('.')

from utils import config_util

class Config:
    def __init__(self):
        # with open("config.json", encoding='utf-8') as f:
        #     config_info = json.load(f)
        #     self.__api_key =  config_info["api-key"]
        self.__api_key = config_util.key_chatgpt_api_key
        pass

    @property
    def api_key(self) -> str:
        return self.__api_key
        
CONFIG = Config()

'''
{
    "api-key": "sk-xxx"
}
'''