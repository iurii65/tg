from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

admin_router = Router()

@admin_router.message(Command('menu'))
async def cmd(message: Message):
    await message.answer(text='Хрен тебе, а не меню')