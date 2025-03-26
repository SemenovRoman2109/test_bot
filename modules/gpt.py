"""
Модуль для роботи з API OpenAI.

У цьому файлі прописана логіка взаємодії бота з серверами OpenAI, що дозволить
боту формувати відповіді на основі ШІ ChatGPT.
"""

from openai import AsyncOpenAI
from dotenv import load_dotenv
import os

# Завантажити вміст файлу ".env"
load_dotenv()
# Отримати секртений ключ з файлу .env що, дає доступ до роботи з API OpenAI 
OPENAI_SECRET_KEY = os.getenv('OPENAI_SECRET_KEY')
# Об'єкт для взаємодії з клієнтом API OpenAI
client_openAI = AsyncOpenAI(
    api_key=OPENAI_SECRET_KEY
)

async def get_response_from_chatgpt(question):
    '''Функція відповідає за формування запиту до серверів OpenAI
    з метою отримання відповіді, згеренованої на основі ChatGPT.'''

    # Об'єкт response, що зберігає відповідь від chatGPT
    response = await client_openAI.chat.completions.create(
        model="ft:gpt-4o-mini-2024-07-18:worldit::BFTfusXq", # Модель GPT, що буде застосована для обробки запитання
        messages=[{
            "role": "user", # Вказати, що запитання буде від користувача
            "content": question # Текст запитання
        }]
    )
    # Повернути текст відповіді
    return response.choices[0].message.content

