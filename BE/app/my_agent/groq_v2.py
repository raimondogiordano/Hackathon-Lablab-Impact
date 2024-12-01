from groq import Groq
import random
from langchain.chains import ConversationChain, LLMChain
from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain_core.messages import SystemMessage
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from app.my_agent.utils.tools import tools

class ConversationMemory:
    
    def __init__(self, window_size: int = 5):
        self.memory = ConversationBufferWindowMemory(window_size=window_size)
    
    def get_memory(self):
        return self.memory

    def update_memory(self, chat_history):
        
        self.memory.chat_memory.add_user_message(chat_history)

class PromptManager:
    
    @staticmethod
    def create_prompt(system_prompt: str):
        return ChatPromptTemplate.from_messages(
            [
                SystemMessage(content=system_prompt),
                MessagesPlaceholder(variable_name="chat_history"),
                HumanMessagePromptTemplate.from_template("{human_input}"),
            ]
        )

class GroqLlama:
    def __init__(self, model=None, prompt_manager=None, memory_manager=None, tools=None):
        # Iniezione delle dipendenze per flessibilità
        self.model = model or ChatGroq(model_name="llama-3.1-70b-versatile")
        self.prompt_manager = prompt_manager or PromptManager()
        self.memory_manager = memory_manager or ConversationMemory()
        self.tools = tools

    def ask(self, user_question: str, system_prompt: str):
        # Creazione del prompt dinamicamente tramite il PromptManager
        prompt = self.prompt_manager.create_prompt(system_prompt)
        
        # Creazione della conversazione
        conversation = LLMChain(
            llm=self.model,
            prompt=prompt,
            verbose=True,
            memory=self.memory_manager.get_memory(),
            tools=self.tools,
        )
        
        response = conversation.predict(human_input=user_question)
        # Aggiorna la memoria della conversazione
        self.memory_manager.update_memory(user_question)
        return response

    def completion_task(self, completion_prompt: str):
        
        # Utilizza il modello per ottenere il completamento del testo
        response = self.model.predict(completion_prompt)
        return response

    def __call__(self, task_type: str, **kwargs):
        
        if task_type == "conversation":
            return self.ask(kwargs.get("user_question"), kwargs.get("system_prompt"))
        elif task_type == "completion":
            return self.completion_task(kwargs.get("completion_prompt"))
        else:
            raise ValueError(f"Task type '{task_type}' non supportato.")

