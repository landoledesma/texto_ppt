import openai
import os
from dotenv import load_dotenv

# Cargando variables de entorno
load_dotenv("token.env")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
openai.api_key = os.getenv("OPENAI_API_KEY")

def slide_title(topic):
    prompt = f"Genera 5 titulos de slides para el tema dado '{topic}'."
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = prompt,
        max_tokens = 200
    )
    return response['choices'][0]['text'].split("\n")

def slide_content(slide_title):
    prompt = f"Genera contenido para cada titulo del slide  '{slide_title}'."
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = prompt,
        max_tokens = 500
    )
    return response['choices'][0]['text']
