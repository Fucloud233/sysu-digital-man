import sys
sys.path.append(".")

from ai_module.enhance.bots.gpt_bot import GPTBot as Bot

def main():
    bot = Bot()
    while True:
        question = input("You: ")
        if question == "exit":
            break
        
        answer = bot.talk(question)
        print(f"Bot: {answer}")


if __name__ == '__main__':
    main()
        
        