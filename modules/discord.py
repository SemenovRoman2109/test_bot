"""
Модуль для роботи з API Discord.

У цьому файлі прописана логіка взаємодії бота з Discord-сервером (отримання,
обробка та відправка повідомлень на сервер).
"""

from discord import Intents, Client
from dotenv import load_dotenv
import os
from .gpt import get_response_from_chatgpt

# Завантажити вміст файлу ".env"
load_dotenv()
# Отримати токен, що дає доступ до керування Discord-ботом, з файлу .env
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

# Об'єкт, що задає доступ боту до різних подій Discord. 
intents = Intents.default()
# Встановити боту доступ до читання контенту повідомлень
intents.message_content = True
# Об'єкт бота
bot_client = Client(intents=intents)

# Декоратор @bot_client.event вказує, що функція on_ready() буде обробником подій
@bot_client.event
async def on_ready():
    '''Функція-подія, що відпрацьовує, коли бот запущено'''
    
    # Вивести повідомлення про запуск бота
    print(f'Бот {bot_client.user} запущено!')

# Декоратор @bot_client.event вказує, що функція on_message() буде обробником подій
@bot_client.event
async def on_message(message):
    '''Функція-подія, що відпрацьовує, коли від користувачів надходить повідомлення'''

    # Якщо автором повідомлення не є сам бот
    if message.author != bot_client.user:
        # Отримати контент повідомлення від користувача
        message_content = message.content
        # Отримати відповідь від ChatGPT
        response = await get_response_from_chatgpt(message_content)
        # Отримати об'єкт повідомлення, на яке треба відповісти, за його id
        message_for_reply = await message.channel.fetch_message(message.id)
        # Надіслати відповідь на повідомлення користувача
        await message_for_reply.reply(response)

    




