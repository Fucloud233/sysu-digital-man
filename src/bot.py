import openai
from abc import abstractmethod
from enum import Enum
from datetime import datetime

from config import CONFIG
from dboperator import DBOPT
from utils import cal_time

openai.api_key = CONFIG.api_key

sys_prompt = '''你是中山大学的学生，现在担任中山大学的介绍官，请注意态度要温文尔雅，风趣幽默，文明礼貌。
    回答问题时也可以适当扩展内容，但请注意答案长度的，请控制在20字内。'''
prompt = "'''{}'''\n以上是你可能会需要的知识,请用50字以内的口语化文本回答以下同学们提出的问题：\n{}"

'''  '''
# sorry_prompt = "{}\n以上是同学向你问的问题，请简要说明对这个问题的感受，注意你是中山大学介绍官，并重新考虑是否要拒绝回答这个问题，控制回答字数在20字以内"

sorry_prompt = "{}\n以上是同学向你问的问题，你可能不需要回答他，" \
    "在必要时使用口语化的表达委婉地告诉他不想回答这个问题，控制回答字数在20字以内"


class BotType(Enum):
    GPT = 0,
    Qianwen = 1,


class Bot:
    def __init__(self, type: BotType):
        self.messages = []
        self.type = type

    def talk(self, question: str):
        begin_tick = datetime.now()

        query_result  = DBOPT.query(question, 5)

        print("[debug] Use ID: ", query_result['ids'])
        print("[debug] Distance:", query_result['distances'])

        query_tick = datetime.now()

        # 如果距离过大 说明问题和中山大学没什么关系
        if query_result['distances'][0][0] > 1:
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

        print("[debug] Q/G/Total: {}/{}/{}".format(
            cal_time(begin_tick, query_tick),
            cal_time(query_tick, end_tick),
            cal_time(begin_tick, end_tick)
        ))

        return answer
    
    @abstractmethod
    def _call_api(self, prompt: str):
        pass

# Load your API key from an environment variable or secret management service


class GPTBot(Bot):
    def __init__(self):
        super().__init__(BotType.GPT)
        self.model = "gpt-3.5-turbo"
        self.messages = []

    def _call_api(self, prompt: str):
        response = openai.ChatCompletion.create(
            model = self.model,
            messages = [
                {"role": "system", "content": sys_prompt},
                {"role": "user", "content": prompt},
            ],
            temperature = 0
        )
    
        return response['choices'][0]['message']['content']