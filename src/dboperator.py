import chromadb
import pandas as pd

from chromadb.utils import embedding_functions

COLLECTION_NAME = "test-documents"
DATA_PATH = "data/wiki_data.csv"

class DBOperator:
    def __init__(self, is_persistend=True):
        sentence_transformer = \
            embedding_functions.SentenceTransformerEmbeddingFunction('paraphrase-multilingual-MiniLM-L12-v2')

        if is_persistend:
            self.client = chromadb.PersistentClient(path="model/chromadb")
        else:
            self.client = chromadb.Client()
        
        self.collection = self.client.get_or_create_collection(COLLECTION_NAME, \
            embedding_function=sentence_transformer)
        
        if self.collection.count() == 0:
            self.__load_documents(DATA_PATH)

    def __load_documents(self, data_path: str):
        df = pd.read_csv(data_path, dtype=str)
        # 对id预处理
        ids = df["id"].to_list()
        documents = df['document'].to_list()
        self.add_documents(documents, ids)

    def add_documents(self, documents, ids):
        self.collection.add(
            documents=documents,
            ids=ids
        )

    def query(self, query_text, n: int=1):
        # print(self.collection.count())

        return self.collection.query(
            query_texts = query_text,
            n_results = n
        )

