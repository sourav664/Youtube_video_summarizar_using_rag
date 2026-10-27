from langchain_openai import ChatOpenAI
from langchain_openai.embeddings import OpenAIEmbeddings



def initialize_openai_llm(model_name, API_KEY):
    # Create and return an instance of the WatsonxLLM with the specified configuration
    return ChatOpenAI(
        model=model_name,
        temperature=0.7,
        api_key=API_KEY       
    )
 
 
 
def setup_embedding_model(embedding_model, API_KEY):
    # Create and return an instance of OpenAiEmbeddings with the specified configuration
    return OpenAIEmbeddings(
       model=embedding_model,
       api_key=API_KEY
    )