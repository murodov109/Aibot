import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor

API_TOKEN = 'YOUR_BOT_API_TOKEN'

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dispatcher = Dispatcher(bot, storage=MemoryStorage())

# Define states
class Form(StatesGroup):
    name = State()  # User will input their name
    age = State()   # User will input their age

@dispatcher.message_handler(commands='start')
async def cmd_start(message: types.Message):
    await Form.name.set()
    await message.reply("Hi! What's your name?")

@dispatcher.message_handler(state=Form.name)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await Form.next()
    await message.reply("Got it! How old are you?")

@dispatcher.message_handler(lambda message: not message.text.isdigit(), state=Form.age)
async def process_age_invalid(message: types.Message):
    return await message.reply("Age should be a number!")

@dispatcher.message_handler(lambda message: message.text.isdigit(), state=Form.age)
async def process_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = int(message.text)
    await message.reply(f"Nice to meet you {data['name']}! You are {data['age']} years old.")
    await state.finish()

@dispatcher.middleware_handler()
async def my_middleware(dispatcher: Dispatcher, _):
    pass  # Implement middleware logic here

if __name__ == '__main__':
    executor.start_polling(dispatcher, skip_updates=True)