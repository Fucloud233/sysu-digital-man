import sys
sys.path.append("./ai_module")
sys.path.append("./ai_module/enhance")

from dboperator import DBOPT

# 预加载DBOPT
if DBOPT.is_empty:
    DBOPT.load_documents('data/sysu_data.csv')

from bots.gpt_bot import GPTBot
# [ignore] 暂时该模型的调用
# from bots.rwkv_bot import RWKVBot
from bots.rwkv_api_bot import RWKVApiBot
from bots.qianfan_bot import QianfanBot
from bots.type import BotType

modules = {
    # "nlp_yuan": nlp_yuan, 
    # "nlp_gpt": nlp_gpt,
    "chatgpt": BotType.GPT,
    # "nlp_rasa": nlp_rasa,
    # "nlp_VisualGLM": nlp_VisualGLM,
    # "nlp_lingju": nlp_lingju,

    # [ignore] 暂时忽略RWKV模型的调用
    # "rwkv": BotType.RWKV,
    
    "rwkv_api": BotType.RWKVApi,
    "qianfan": BotType.Qianfan
    # "nlp_chatglm2": nlp_ChatGLM2
}

# 根据机器人类别返回对象
def get_bot(input_module: str):
    bot_type = modules.get(input_module)
    
    match bot_type:
        case BotType.GPT:
            return GPTBot()
        # case BotType.RWKV:
        #     return RWKVBot()
        case BotType.RWKVApi:
            return RWKVApiBot()
        case BotType.Qianfan:
            return QianfanBot()
        case _: 
            return None