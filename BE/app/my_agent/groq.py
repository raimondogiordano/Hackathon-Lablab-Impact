from langchain.agents import initialize_agent, Tool
from groq import Groq
from pydantic import BaseModel
from langchain_groq import ChatGroq

# Configurazione Llama con Groq
class GroqLlama:
    def __init__(self, model_name: str):
        self.groq_client = Groq(model_name=model_name)
        

    def __call__(self, prompt: str) -> str:
        # Esegui la richiesta tramite Groq per accelerare l'elaborazione
        try:
            response = self.groq_client.execute(prompt)
            return response['output']
        except Exception as e:
            print(f"Errore con Groq: {str(e)}")
            return "Errore nella risposta dell'agente."

# Istanzia GroqLlama
def initialize_agent_groq(model_name: str,tools: list[Tool],agent: str):
    llama_with_groq = GroqLlama(model_name=model_name)
    agent = initialize_agent(
        tools=tools,
        llm=llama_with_groq,
        agent="chat-conversational",
        verbose=True
    )
    return agent

def call_groq(tools: list[Tool],messages: list[dict],model_name:str="llm",tool_choice:str="auto",response_format:dict={"type": "text"},temperature:int=1,top_p:int=1,stream:bool=False,stop:str=None,response_model:BaseModel|None=None):
    if response_format.type == "json_object" and response_model is not None:
        messages[0]=messages[0].content=messages[0].content + f"\n The JSON object must use the schema: {json.dumps(Recipe.model_json_schema(), indent=2)}"
        print(messages[0].content)
    llama_with_groq = GroqLlama(model_name=model_name).groq_client.chat.completions.create(
        model=model_name,
        messages=messages,
        response_format=response_format,
        temperature=temperature,
        top_p=top_p,
        stream=stream,
        stop=stop,
    )


