import os 
import json
import asyncio
from aiogram import Bot
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import Message


def write_to_json(file_path, data):
    with open(file_path, "w") as json_file:
        json.dump(data, json_file, indent=4)  # indent=4 для читабельности


# Функция для чтения данных из JSON файла
def read_from_json(file_path):
    with open(file_path, "r") as json_file:
        data = json.load(json_file)
    return data


TOKEN = os.getenv('toketBotTG')
if not TOKEN:
    raise ValueError("Токен Telegram бота не найден!")



chat_ids = []
BOT = Bot(token=TOKEN)
DP = Dispatcher()


@DP.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    if message.chat.id not in chat_ids:
        chat_ids.append(message.chat.id)
    print(chat_ids)
    await message.answer("Привет! Я ваш бот. Чем могу помочь?")


# @dp.message_handler()
# async def echo(message: types.Message):
#     await message.answer(f"Вы написали: {message.text}")


def bot_service_run():
    print("RUNNING BOT")
    global DP
    global BOT
    asyncio.run(DP.start_polling(BOT))
