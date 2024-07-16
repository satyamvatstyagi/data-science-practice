from fastapi import HTTPException
from pydantic import BaseModel
from .embeddings import initialize_embeddings
from .storage import initialize_pinecone, PineconeStore
from langchain.chains import RetrievalQAWithSourcesChain
from langchain_openai import OpenAI


class QueryRequest(BaseModel):
    query: str


class QueryResponse(BaseModel):
    answer: str
    sources: str


async def query_system_endpoint(query_request: QueryRequest):
    query = query_request.query

    # get the docsearch from pinecone store
    store = PineconeStore.get_pinecone_store()
    if not store:
        embeddings = initialize_embeddings()
        store = initialize_pinecone(embeddings)

    retriever = store.as_retriever()
    llm = OpenAI(temperature=0.7, max_tokens=500)
    chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=retriever)

    response = chain({"question": query}, return_only_outputs=True)
    print(response)

    if not response:
        raise HTTPException(status_code=400, detail="Failed to process query")

    # Check the response structure and adjust accordingly
    answer = response.get('answer')
    sources = response.get('sources')
    if answer is None or sources is None:
        raise HTTPException(
            status_code=500, detail="Invalid response format from chain")

    return QueryResponse(answer=answer, sources=sources)
