import torch
from ringrwkv.configuration_rwkv_world import RwkvConfig
from ringrwkv.rwkv_tokenizer import TRIE_TOKENIZER
from ringrwkv.modehf_world import RwkvForCausalLM

from enhance.bots.bot import Bot, BotType

model = RwkvForCausalLM.from_pretrained("RWKV-4-World-1.5B")
#model = RwkvForCausalLM.from_pretrained("RWKV-4-World-3B")
#model = RwkvForCausalLM.from_pretrained("RWKV-4-World-0.4B")
# 设置模型位置
tokenizer = TRIE_TOKENIZER('./model/ringrwkv/rwkv_vocab_v20230424.txt')

class RWKVBot(Bot):
    def __init__(self):
        super().__init__(BotType.RWKV)

    def _call_api(self, prompt: str):
        prompt = f'{self.sys_prompt}\n{prompt}'
        input_ids = tokenizer.encode(prompt)
        input_ids = torch.tensor(input_ids).unsqueeze(0)

        out = model.generate(input_ids, max_new_tokens=20)

        out_list = out[0].tolist()
        for i in out_list:
            if i==0:
                out_list.remove(i)
        
        answer = tokenizer.decode(out_list)
        answer = answer.replace(prompt, "", 1)
    
        return answer
