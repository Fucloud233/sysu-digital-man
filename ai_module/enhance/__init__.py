import sys
sys.path.append("./ai_module")
sys.path.append("./ai_module/enhance")

from dboperator import DBOPT

# 预加载DBOPT
if DBOPT.is_empty:
    DBOPT.load_documents('data/wiki_data.csv')

from bots.gpt_bot import GPTBot
# [ignore] 暂时该模型的调用
# from bots.rwkv_bot import RWKVBot
from bots.rwkv_api_bot import RWKVApiBot
from bots.qianfan_bot import QianfanBot
from bots.type import BotType

# 根据机器人类别返回对象
def get_bot(bot_type: BotType):
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