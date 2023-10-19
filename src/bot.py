import openai
from datetime import datetime

from config import CONFIG
from dboperator import DBOPT
from utils import cal_time

openai.api_key = CONFIG.api_key

sys_prompt = '''你是中山大学的学生，现在担任中山大学的介绍官，请注意态度要温文尔雅，风趣幽默，文明礼貌。
    回答问题时也可以适当扩展内容，但请注意答案长度的，请控制在20字内。'''
prompt = "'''{}'''\n以上是你可能会需要的知识,请用50字以内的口语化文本回答以下同学们提出的问题：\n{}"

'''  '''
sorry_prompt = "{}\n以上是同学向你问的问题，请简要说明对这个问题的感受，注意你是中山大学介绍官并用20字以内的口语化的方式委婉地拒绝回答他，"

class Bot:
    def __init__(self):
        self.model = "gpt-3.5-turbo"
        self.messages = []

    def talk(self, question: str):
        begin_tick = datetime.now()

        query_result  = DBOPT.query(question, 5)

        print("[debug] Use ID: ", query_result['ids'])
        print("[debug] Distance:", query_result['distances'])

        query_tick = datetime.now()

        # 如果距离过大 说明问题和中山大学没什么关系
        if query_result['distances'][0][0] > 10:
            cur_prompt = sorry_prompt.format(question)
        else:

            documents = query_result['documents']
            cur_prompt = prompt.format(documents, question)

        try:
            response = openai.ChatCompletion.create(
                model = self.model,
                messages = [
                    {"role": "system", "content": sys_prompt},
                    {"role": "user", "content": cur_prompt},
                ],
                temperature = 0
            )
        except Exception:
            return '不好意思，系统出了些问题，请换个问题问吧？'
        
        end_tick = datetime.now()

        print("[debug] Q/G/Total: {}/{}/{}".format(
            cal_time(begin_tick, query_tick),
            cal_time(query_tick, end_tick),
            cal_time(begin_tick, end_tick)
        ))

        return response['choices'][0]['message']['content']

# Load your API key from an environment variable or secret management service

