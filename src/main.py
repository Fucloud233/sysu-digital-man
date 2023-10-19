import fire 
import sys

from dboperator import DBOPT
from bot import Bot


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

def main(reload: bool=False):
    # 重新加载向量数据库
    if reload: DBOPT.reload_documents(WIKI_DATA_PATH)

    bot = Bot()
    while True:
        question = input("Please input question：")
        if question == 'exit':
            sys.exit(0)

        answer = bot.talk(question)
        print("Answer: ", answer)


if __name__ == '__main__':
    fire.Fire(main())