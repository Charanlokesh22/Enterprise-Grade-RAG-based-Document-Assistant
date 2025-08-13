Project Title: Enterprise-Grade RAG-based Document Assistant

Description:
This project implements a production-grade, domain-specific AI assistant for technical document Q&A. It uses Retrieval-Augmented Generation (RAG) and multi-step agent workflows to deliver context-aware answers. Semantic vector search retrieves relevant document context from Pinecone, and Azure OpenAI provides the LLM-powered responses. Terraform automates deployment, while Arize AI and WhyLabs enable real-time monitoring, drift detection, and explainability.

Tech Stack:
- Python
- LangChain
- Hugging Face Transformers
- LangGraph
- Pinecone
- Azure OpenAI Service
- Arize AI
- WhyLabs
- Terraform

Features:
- Retrieval-Augmented Generation for domain-specific document retrieval
- Vector search with Pinecone for high semantic accuracy
- Multi-step agent workflows using LangChain and LangGraph
- LLM-powered responses via Azure OpenAI
- Real-time monitoring with Arize AI and WhyLabs
- Infrastructure as Code deployment with Terraform

Setup Instructions:
Clone the repository:
git clone https://github.com/Charanlokesh22/enterprise-rag-assistant.git

Navigate into the project folder:
cd enterprise-rag-assistant

Install dependencies:
pip install -r requirements.txt

Set Environment Variables:
- export PINECONE_API_KEY=your_pinecone_api_key
- export AZURE_OPENAI_KEY=your_azure_openai_key
- export AZURE_OPENAI_ENDPOINT=your_azure_openai_endpoint
- export ARIZE_API_KEY=your_arize_api_key
- export WHYLABS_API_KEY=your_whylabs_api_key



# Download spaCy model
python -m spacy download en_core_web_sm

# Run the application
python main.py
