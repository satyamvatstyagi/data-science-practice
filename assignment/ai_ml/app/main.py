from fastapi import FastAPI
from app.routers import extract_router, query_router

app = FastAPI()

app.include_router(extract_router, prefix="/extract", tags=["extract"])
app.include_router(query_router, prefix="/query", tags=["query"])


@app.get("/")
async def root():
    return {"message": "Welcome to the QA bot API"}
