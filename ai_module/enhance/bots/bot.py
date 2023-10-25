import openai
from abc import abstractmethod
from datetime import datetime

from config import CONFIG
from dboperator import DBOPT
from bots.type import BotType
from utils.util import cal_time


SYS_PROMPT = '''你是中山大学的学生，现在担任中山大学的介绍官，请注意态度要温文尔雅，风趣幽默，文明礼貌。
    回答问题时也可以适当扩展内容，但请注意答案长度的，请控制在20字内。'''
prompt = "你现在知道这些知识：{}\n有同学问你这个问题：{}\n作为中山大学的介绍官，请用口语化文本清晰地回答同学们提出的问题，并一定要控制回答再50字以内！"

'''  '''
# sorry_prompt = "{}\n以上是同学向你问的问题，请简要说明对这个问题的感受，注意你是中山大学介绍官，并重新考虑是否要拒绝回答这个问题，控制回答字数在20字以内"

sorry_prompt = "{}\n以上是同学向你问的问题，请你再考虑一下是否需要回答这个问题。" \
    "如果与中山大学不怎么相关，请注意你是中山大学介绍官的身份，并委婉地拒绝他。" \
    "无论是什么问题，请将回答字数控制在20字以内"

class Bot:
    def __init__(self, type: BotType):
        self.messages = []
        self.type = type
        self.sys_prompt = SYS_PROMPT
        openai.api_key = CONFIG.api_key

    def talk(self, question: str):
        begin_tick = datetime.now()

        query_result  = DBOPT.query(question, 3)

        print("[debug] Use ID: ", query_result['ids'])
        print("[debug] Distance:", query_result['distances'])

        query_tick = datetime.now()

        # 如果距离过大 说明问题和中山大学没什么关系
        if round(query_result['distances'][0][0]) > 1.0:
            cur_prompt = sorry_prompt.format(question)
        else:
            documents = query_result['documents']
            cur_prompt = prompt.format(documents, question)

        try:
            answer = self._call_api(cur_prompt)
        except openai.APIError as e:
            print("[debug]", e)
            return '不好意思，系统出了些问题，请换个问题问吧？'
        
        end_tick = datetime.now()

        print("[debug] Time used by Bot: %.3fs"%cal_time(begin_tick, end_tick))

        return answer
    
    @abstractmethod
    def _call_api(self, prompt: str):
        pass

# Load your API key from an environment variable or secret management service
