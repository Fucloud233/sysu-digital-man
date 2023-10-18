import pandas as pd
import pprint

from dboperator import DBOperator
from bot import Bot

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

def main():
    bot = Bot()
    question = input("Please input question：")
    answer = bot.talk(question)
    print("Answer: ", answer)


if __name__ == '__main__':
    main()