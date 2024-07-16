from fastapi import HTTPException
from .embeddings import initialize_embeddings
from .storage import initialize_pinecone
from .utils import extract_text_from_pdf, split_data_into_chunks


async def load_pdf_endpoint(pdf_path: str):
    print(pdf_path)
    data = extract_text_from_pdf(pdf_path)
    if not data:
        raise HTTPException(
            status_code=400, detail="Failed to extract text from PDF")

    print('Number of documents:', len(data))
    docs = split_data_into_chunks(data)
    if not docs:
        raise HTTPException(
            status_code=400, detail="Failed to split text into chunks")
    print('Number of chunks:', len(docs))

    embeddings = initialize_embeddings()
    store = initialize_pinecone()
    store.store_documents(docs, embeddings)

    return {"message": "PDF processed and loaded successfully", "num_chunks": len(docs)}
