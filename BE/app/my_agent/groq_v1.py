
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

class GroqLlama:
    def __init__(self,prompt:str, model_name: str="llama-3.1-70b-versatile"):
        self.groq_chat = ChatGroq(model_name=model_name)
        self.prompt = prompt


    def ask(self, user_question:str):
        memory = ConversationBufferWindowMemory(window_size=5)
        prompt = ChatPromptTemplate.from_messages(
            [
                SystemMessage(
                    content=system_prompt
                ),  

                MessagesPlaceholder(
                    variable_name="chat_history"
                ), 

                HumanMessagePromptTemplate.from_template(
                    "{human_input}"
                ),  
            ]
        )

        conversation = LLMChain(
            llm=self.groq_chat, 
            prompt=self.prompt,  
            verbose=True,   
            memory=memory,  
            tools=tools,
            
        )
        
        response = conversation.predict(human_input=user_question)
        return response
    
    def __call__(self):
        return self.ask(self.prompt)