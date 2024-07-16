# QA Bot with FastAPI

## Overview

This project is a QA bot that can extract text from PDFs, generate embeddings, store them in a vector database, and retrieve relevant text chunks based on user queries. It uses FastAPI for the API, Pinecone for the vector database, and integrates with OpenAI's GPT for refining user queries.

## Features

- Extract text from PDF files and split into chunks.
- Generate embeddings using OpenAI embeddings.
- Store embeddings in Pinecone vector database.
- Query the system to retrieve relevant text chunks.
- Maintain conversation context.
- Use additional tools like Wikipedia and LLM-math for enhanced queries.

## Directory Structure

```bash
├── Dockerfile
├── Interim_Budget.pdf
├── README.md
├── ai_ml_assginment.ipynb
├── app
│   ├── Interim_Budget.pdf
│   ├── __init__.py
│   ├── agent.py
│   ├── conversation.py
│   ├── dependencies.py
│   ├── embeddings.py
│   ├── extract.py
│   ├── main.py
│   ├── query.py
│   ├── routers.py
│   ├── storage.py
│   └── utils.py
├── docs
│   ├── flow.puml
│   ├── sequence.png
│   └── seuence.puml
└── requirements.txt
```

# QA Bot with FastAPI

This project is a QA bot built with FastAPI to extract text from PDFs, generate embeddings, and store them in a vector database. Users can query the system, which retrieves relevant text chunks based on similarity scores. The system integrates with a GPT model for refining user queries.

## Setup

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables:
    ```bash
    export OPENAI_API_KEY="your-openai-api-key"
    export PINECONE_API_KEY="your-pinecone-api-key"
    ```

4. Run the FastAPI application:
    Running the Application

There are several ways to run the application:

### Using Python Environment

1. **Install the Python environment**:
   Ensure you have Python 3.9 installed.

2. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```sh
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```

### Using Docker Locally

1. **Build the Docker image locally**:
   ```sh
   docker build -t qa-bot-service-image:1.0.0 .
   ```

2. **Run the container**:
   ```sh
   docker run -tid --name qa-bot-service-container -p 8000:8000 qa-bot-service-image:1.0.0
   ```

3. **Exec into the container**:
   Check the container ID via `docker ps` and run:
   ```sh
   docker exec -ti <container_id> sh
   ```

4. **Run the application inside the container**:
   ```sh
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```

### Using Docker Image from Docker Hub

1. **Pull the Docker image from Docker Hub**:
   ```sh
   docker pull satyamvatstyagi/qa-bot-service-image:1.0.0
   ```

2. **Run the container**:
   ```sh
   docker run -tid --name qa-bot-service-container -p 8000:8000 satyamvatstyagi/qa-bot-service-image:1.0.0
   ```

3. **Exec into the container**:
   Check the container ID via `docker ps` and run:
   ```sh
   docker exec -ti <container_id> sh
   ```

4. **Run the application inside the container**:
   ```sh
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```

## Accessing the Application

Once the application is running, you can access it at:
```
http://localhost:8000
```

## Endpoints

### Load PDF
- **URL:** `/extract/load-pdf/`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
        "pdf_path": "path/to/your/pdf"
    }
    ```
- **Response:**
    ```json
    {
        "message": "PDF processed and loaded successfully",
        "num_chunks": 42
    }
    ```

### Query System
- **URL:** `/query/`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
        "query": "Who is finance minister of India?"
    }
    ```
- **Response:**
    ```json
    {
        "response": "The finance minister of India is...",
        "source": "Source document content"
    }
    ```

## Architecture

1. Extract text from PDFs, segment it into chunks, and generate embeddings.
2. Store embeddings in Pinecone vector database.
3. Retrieve relevant text chunks based on user queries.
4. Integrate with GPT model to refine user queries.

## Performance Evaluation

- Measure the time taken for PDF loading and text extraction.
- Evaluate the accuracy of query responses.

## Video Demonstration

[Link to video](https://nagarro-my.sharepoint.com/:v:/r/personal/satyam_vats_nagarro_com/Documents/NAGP/Assignment/DataScience_AI_ML/Assignment_3144985_AI_ML.mov?csf=1&web=1&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=fjcDqJ)
