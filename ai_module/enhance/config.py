from bots.type  import BotType
from utils import config_util

class Config:
    def __init__(self):
        # with open("config.json", encoding='utf-8') as f:
        #     config_info = json.load(f)
        #     self.__api_key =  config_info["api-key"]
        self.__openai_api_key = config_util.key_chatgpt_api_key
        self.__qianfan_api_key = config_util.key_qianfan_api_key
        self.__qianfan_api_secret = config_util.key_qianfan_api_secret
        pass

    def api_key(self, bot_type: BotType) -> (str, str):
        key = None
        secret = None
        match bot_type:
            case BotType.GPT: key = self.__openai_api_key
            case BotType.Qianfan: 
                key = self.__qianfan_api_key
                secret = self.__qianfan_api_secret
            case _: raise ValueError(f'The key of "{bot_type}" not found!')

        return (key, secret)
    
    @property
    def openai_api_key(self):
        return self.__openai_api_key
        
    
CONFIG = Config()

'''
{
    "api-key": "sk-xxx"
}
'''