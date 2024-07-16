import openai
from pinecone import Pinecone, ServerlessSpec
from langchain_community.llms import OpenAI
from langchain_community.vectorstores import Pinecone as PineconeVectorStore
from langchain.memory import ConversationBufferMemory


# Initialize OpenAI API
openai.api_key = 'your-openai-api-key'

# Initialize Pinecone
pinecone_api_key = "accdbcc1-d799-47ba-9ae2-440e59b4f774"
pinecone_environment = "us-east-1"

pinecone = Pinecone(api_key=pinecone_api_key)

# Define Pinecone index dimensions
INDEX_NAME = "qabot"
DIMENSIONS = 1536

# Create Pinecone index if not exists
if INDEX_NAME not in pinecone.list_indexes().names():
    pinecone.create_index(
        name=INDEX_NAME,
        dimension=DIMENSIONS,
        metric='euclidean',
        spec=ServerlessSpec(
            cloud='aws',
            region=pinecone_environment
        )
    )

# Initialize the language model
llm = OpenAI(api_key="your-openai-api-key")

# Initialize memory
memory = ConversationBufferMemory(k=5)
