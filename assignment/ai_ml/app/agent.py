from fastapi import APIRouter
from pydantic import BaseModel
from langchain.agents import initialize_agent, load_tools, AgentType
from langchain_openai import OpenAI

agent_router = APIRouter()


class AgentQueryRequest(BaseModel):
    query: str


class AgentQueryResponse(BaseModel):
    response: str


llm = OpenAI(temperature=0.7, max_tokens=500)
tools = load_tools(["wikipedia", "llm-math"], llm=llm)
agent = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)


@agent_router.post("/", response_model=AgentQueryResponse)
async def agent_query(query_request: AgentQueryRequest):
    query = query_request.query
    response = agent({"input": query})
    return AgentQueryResponse(response=response["output"])
