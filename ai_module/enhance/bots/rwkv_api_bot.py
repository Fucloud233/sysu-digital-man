import requests
import time

from enhance.bots.bot import Bot, BotType


class RWKVApiBot(Bot):
    def __init__(self):
        super().__init__(BotType.RWKV)
        self.api_url = "https://rwkv.ai-creator.net/chntuned/v1/chat/completions"

    def _call_api(self, prompt: str):
        session = requests.Session()

        # 对话列表
        message=[
            {"role": "system", "content": self.sys_prompt},
            {"role": "user", "content": prompt}
        ]

        # 生成http请求数据
        data = {
            # "model":model_engine,
            "messages":message,
            "temperature":0.3,
            "max_tokens":2000,
            "user":"live-virtual-digital-person"
        }
        headers = {
            'content-type': 'application/json', 
            'Authorization': 'Bearer '
        }

        try:
            response = session.post(self.api_url, json=data, headers=headers)
            response.raise_for_status()  # 检查响应状态码是否为200

            result = eval(response.text)
            response_text = result["choices"][0]["message"]["content"]
            
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")
            response_text = "抱歉，我现在太忙了，休息一会，请稍后再试。"


        # print("接口调用耗时 :" + str(time.time() - starttime))

        return response_text.strip()

