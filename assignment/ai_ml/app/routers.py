from fastapi import APIRouter
from app.extract import load_pdf_endpoint
from app.query import query_system_endpoint

extract_router = APIRouter()
extract_router.post("/load-pdf/")(load_pdf_endpoint)

query_router = APIRouter()
query_router.post("/")(query_system_endpoint)
