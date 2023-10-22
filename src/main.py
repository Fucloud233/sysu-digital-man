import fire
import sys

from dboperator import DBOPT
from bot import GPTBot


WIKI_DATA_PATH = "data/wiki_data.csv"

# def main():
#     df = pd.read_csv('./data.csv')
#     ids = df["id"].to_list()
#     documents = df['document'].to_list()

#     # print(ids)
#     # pprint.pprint(documents)

#     operator = DBOperator()
#     operator.add_documents(documents, ids)

#     result = operator.query(["中山大学医疗"])

#     pprint.pprint(result)

def main(reload: bool=False, type: int=0):
    # 重新加载向量数据库
    if reload: 
        print("[debug] The db is reloaded.")
        DBOPT.reload_documents(WIKI_DATA_PATH)
    
    # 配置调用的LLM
    match type:
        case 0: bot = GPTBot()
        
    while True:
        question = input("You: ")
        if question == 'exit':
            sys.exit(0)

        answer = bot.talk(question)
        print("Bot:", answer)


if __name__ == '__main__':
    fire.Fire(main)