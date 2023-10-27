import sys
sys.path.append(".")

from ai_module.enhance import get_bot
from ai_module.enhance.bots.type import BotType

def main():
    bot = get_bot("qianfan")
    while(True):
        question = input("You: ")
        if question == 'exit':
            break

        answer = bot.talk(question)
        print("Bot:", answer)
    
if __name__ == '__main__':
    main()