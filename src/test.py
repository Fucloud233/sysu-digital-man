import chromadb
import pprint

pp = pprint.PrettyPrinter(indent=4)

client = chromadb.Client()

collection = client.create_collection("all-my-documents")

collection.add(
    documents = ["This is document1", "This is document2"],
    metadatas = [{"source": "notion"}, {"source": "google-docs"}],
    ids = ["doc1", "doc2"]
)

results = collection.query(
    query_texts="This is a query document",
    n_results = 2,
)

pp.pprint(results)