import json

class Config:
    def __init__(self):
        with open("config.json", encoding='utf-8') as f:
            config_info = json.load(f)
            self.__api_key =  config_info["api-key"]

    @property
    def api_key(self) -> str:
        return self.__api_key
        
CONFIG = Config()

'''
{
    "api-key": "sk-xxx"
}
'''