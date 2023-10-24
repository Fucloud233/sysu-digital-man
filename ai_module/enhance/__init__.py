import sys
sys.path.append("./ai_module")
sys.path.append("./ai_module/enhance")

from dboperator import DBOPT

# 预加载DBOPT
if DBOPT.is_empty:
    DBOPT.load_documents('data/wiki_data.csv')


from bots.gpt_bot import GPTBot
from bots.qianfan_bot import QianfanBot
from bots.bot import BotType

def get_bot(bot_type: BotType):
    match bot_type:
        case BotType.GPT:
            return GPTBot()
        case BotType.Qianfan:
            return QianfanBot()
        case _: raise TypeError('The type of bot "{}" not found!')