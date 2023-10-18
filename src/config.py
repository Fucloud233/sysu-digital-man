import json

class Config:
    def __init__(self):
        config_info = json.load("config.json")

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