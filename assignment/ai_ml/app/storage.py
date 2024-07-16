import os
import pinecone
from langchain_pinecone import Pinecone


class PineconeStore:
    docsearch = None  # Class variable to store docsearch
    index_name = "qabot"  # Class variable to store index name

    def __init__(self, index_name="qabot"):
        index_name = index_name

    @classmethod
    def store_documents(cls, docs, embeddings):
        cls.docsearch = Pinecone.from_documents(
            documents=docs, embedding=embeddings, index_name=cls.index_name)
        return cls.docsearch

    @classmethod
    def get_pinecone_store(cls):
        if cls.docsearch is not None:
            return cls.docsearch
        else:
            raise ValueError(
                "docsearch has not been initialized. Call store_documents first.")


def initialize_pinecone():
    # pinecone.init(
    #     api_key=os.environ['PINECONE_API_KEY'], environment='us-east-1')
    index_name = "qabot"
    # if index_name not in pinecone.list_indexes():
    #     pinecone.create_index(index_name, dimension=1536)
    return PineconeStore(index_name=index_name)
