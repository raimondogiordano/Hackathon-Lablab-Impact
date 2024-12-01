import requests
from typing import Dict
from langchain_groq import ChatGroq
from groq import Groq


class VisionAnalysisService:
    def __init__(self):
        # Inizializza il modello Llama Vision utilizzando Langchain

        self.llm=Groq()

    def analyze_image_with_llama_vision(self, images: bytes):
        completion = self.llm.chat.completions.create(
            model="llama-3.2-90b-vision-preview",
            messages=[
                {
                    "role": "user",
                    "content": "You are an helpful reader that given a ticket that can be a Fly or Train or Bus can extract the information from the image and return the information in a text. The ticket can be in any language. Follow the following json {'from':Madrid,'to':Barcelona,'date':'2022-12-12 12:00:00'}"
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": "https://img.freepik.com/vettori-premium/carta-d-imbarco-piatto-blu-e-bianco_23-2147588756.jpg?w=996"
                            }
                        }
                    ]
                }
            ],
            response_format={"type": "json_object"},
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=False,
            stop=None,
        )

        print(completion.choices[0].message)

    def _parse_response(self, response: str) -> Dict[str, str]:
        # Analizza la risposta di Llama per estrarre le informazioni
        viaggio_info = {}
        lines = response.split("\n")
        for line in lines:
            if "Destinazione" in line:
                viaggio_info["destinazione"] = line.split(":")[1].strip()
            elif "Data di partenza" in line:
                viaggio_info["data_partenza"] = line.split(":")[1].strip()
            elif "Data di arrivo" in line:
                viaggio_info["data_arrivo"] = line.split(":")[1].strip()
        return viaggio_info


