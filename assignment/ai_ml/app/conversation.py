from fastapi import APIRouter
from pydantic import BaseModel
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import ConversationChain
from langchain_openai import OpenAI

conversation_router = APIRouter()


class ConversationRequest(BaseModel):
    query: str


class ConversationResponse(BaseModel):
    response: str


llm = OpenAI(temperature=0.7, max_tokens=500)
memory = ConversationBufferWindowMemory(k=5)
convo = ConversationChain(llm=llm, memory=memory)


@conversation_router.post("/", response_model=ConversationResponse)
async def conversation(query_request: ConversationRequest):
    query = query_request.query
    response = convo.run(query)
    return ConversationResponse(response=response)
