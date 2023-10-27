import chromadb
import pandas as pd

from config import CONFIG
from chromadb.utils import embedding_functions

COLLECTION_NAME = "test-documents"
DATA_PATH = "data/wiki_data.csv"

OPENAI_EF = embedding_functions.OpenAIEmbeddingFunction(
    api_key=CONFIG.api_key,
    model_name="text-embedding-ada-002"
)

SENTENCE_TRANSFORMER_EF = \
    embedding_functions.SentenceTransformerEmbeddingFunction('distiluse-base-multilingual-cased-v1')

class DBOperator:
    def __init__(self, is_persistend=True):
        if is_persistend:
            self.client = chromadb.PersistentClient(path="model/chromadb")
        else:
            self.client = chromadb.Client()
        
        self.collection = self.client.get_or_create_collection(COLLECTION_NAME, \
            embedding_function=SENTENCE_TRANSFORMER_EF)

        # # 当Collections中没有数据 则需要加载
        # if self.collection.count() == 0:
        #     if data_path == None:
        #         raise ValueError("The path of data is None")
        #     self.__load_documents(data_path)

    def load_documents(self, data_path: str):
        df = pd.read_csv(data_path, dtype=str)
        # 对id预处理
        ids = df["id"].to_list()
        documents = df['document'].to_list()
        self.add_documents(documents, ids)
        # self.collection.update()

    def reload_documents(self, data_path: str):
        # 删除原始colletion后，重新创建
        self.client.delete_collection(COLLECTION_NAME)
        # 记得切换中文Embedding
        self.client.create_collection(COLLECTION_NAME, \
            embedding_function=SENTENCE_TRANSFORMER_EF)
        self.collection = self.client.get_collection(COLLECTION_NAME, \
            embedding_function=SENTENCE_TRANSFORMER_EF)

        self.load_documents(data_path)

    def add_documents(self, documents, ids):
        self.collection.add(
            documents=documents,
            ids=ids
        )
    
    def display(self):
        # self.collection.
        pass

    def query(self, query_text, n: int=1):
        # print(self.collection.count())

        return self.collection.query(
            query_texts = query_text,
            n_results = n
        )
    
    @property
    def is_empty(self):
        return self.collection.count() == 0

DBOPT = DBOperator(True)