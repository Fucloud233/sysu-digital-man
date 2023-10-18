import chromadb
import pandas as pd

from chromadb.utils import embedding_functions

class DBOperator:
    def __init__(self, data_path: str, auto_load: bool=False):
        sentence_transformer = \
            embedding_functions.SentenceTransformerEmbeddingFunction('paraphrase-multilingual-MiniLM-L12-v2')

        self.client = chromadb.Client()
        self.collection = self.client.create_collection("test-documents", \
            embedding_function=sentence_transformer)
        
        # 加载文档
        if auto_load:
            self.load_documents(data_path)

    def load_documents(self, data_path: str):
        df = pd.read_csv(data_path)

        # 对id预处理
        ids: list[str] = df["id"].to_list()
        ids = [ id.split(',') for id in ids]

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

