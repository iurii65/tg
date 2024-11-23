from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

user_router = Router()

#Хендлер на сообщение \start
@user_router.message(CommandStart())
async def start(message: Message):
    await message.answer_photo(photo='https://i.ytimg.com/vi/B_Yx1ZsfjL0/maxresdefault.jpg',
                               caption='Привет! Давай знакомиться, меня зовут Джарвис, а тебя?')

@user_router.message(Command('menu'))
async def cmd(message: Message):
    await message.answer(text='Хрен тебе, а не меню')

@user_router.message(Command('info'))
async def cmd(message: Message):
    await message.answer(text='Здесь будет инфа о Jarvis')


@user_router.message(F.from_user.id == 581558037)
async def mess(message: Message):
    await message.reply(text='Я тебя знаю, ты Даша, девушка моего создателя')

@user_router.message(F.from_user.id == 549040158)
async def mess(message: Message):
    await message.reply(text='Привет, что хотел?') 

#Хендлер на любое другое сообщение кроме \start
@user_router.message()
async def mess(message: Message):
    await message.answer(text='Классное имя! Я попробую его запомнить')

