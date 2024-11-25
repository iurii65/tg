from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

user_router = Router()

class User (StatesGroup):
    name = State()
    number = State()
    birthdate =State()

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

'''
@user_router.message(F.from_user.id == 581558037)
async def mess(message: Message):
    await message.reply(text='Я тебя знаю, ты Даша, девушка моего создателя')

@user_router.message(F.from_user.id == 549040158)
async def mess(message: Message):
    await message.reply(text='Привет, что хотел?') 
'''

@user_router.message(Command('registration'))
async def registr(message: Message, state: FSMContext):
    await state.set_state(User.name)
    await message.answer(f'Как я могу тебя называть незнакомец?')

@user_router.message(User.name)
async def name_reg(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(User.number)
    await message.answer('Теперь мне нужен твой номер, чтобы я мог набрать тебя')

@user_router.message(User.number)
async def phone_reg(message: Message, state: FSMContext):
    await state.update_data(number=message.text)
    await state.set_state(User.birthdate)
    await message.answer('А теперь скажи когда у тебя ДР?, чтобы я смог тебя поздравить')

@user_router.message(User.birthdate)
async def date_reg(message: Message, state: FSMContext):
    await state.update_data(birthdate=message.text)
    data = await state.get_data()
    await message.answer(f'И так что я запомнил. Тебя зовут {data['name']}')
    await state.clear()


#Хендлер на любое другое сообщение кроме \start
@user_router.message()
async def mess(message: Message):
    await message.answer(text='Классное имя! Я попробую его запомнить')
