import openai

from enhance.bots.bot import Bot, BotType
from config import CONFIG

openai.api_key = CONFIG.api_key

class GPTBot(Bot):
    def __init__(self):
        super().__init__(BotType.GPT)
        self.model = "gpt-3.5-turbo"
        self.messages = []

    def _call_api(self, prompt: str):
        response = openai.ChatCompletion.create(
            model = self.model,
            messages = [
                {"role": "system", "content": self.sys_prompt},
                {"role": "user", "content": prompt},
            ],
            temperature = 0
        )
    
        return response['choices'][0]['message']['content']