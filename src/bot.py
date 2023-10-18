import openai
import os
from config import CONFIG

from dboperator import DBOperator

openai.api_key = CONFIG.api_key

sys_prompt = '''你现在是21岁女大学生，目前正在担任中山大学的介绍官，请注意态度要温文尔雅，风趣幽默，文明礼貌。
    回答问题时也可以适当扩展内容，但请注意答案长度的，请控制在20字内。'''
prompt = "'''{}'''\n 以上是你可能会需要的知识,请用50字以内的口语化文本回答以下同学们提出的问题：\n{}"

class Bot:
    def __init__(self):
        self.model = "gpt-3.5-turbo"
        self.messages = []
        self.operator = DBOperator()
    
    def talk(self, question: str):
        query_result  = self.operator.query(question, 5)
        print("[debug] Use ID: ", query_result['ids'])

        documents = query_result['documents']
        cur_prompt = prompt.format(documents, question)

        response = openai.ChatCompletion.create(
            model = self.model,
            messages = [
                {"role": "system", "content": sys_prompt},
                {"role": "user", "content": cur_prompt},
            ]
        )

        return response['choices'][0]['message']['content']
        


# Load your API key from an environment variable or secret management service

