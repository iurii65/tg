import asyncio
import logging

from aiogram import Bot, Dispatcher

from app.user_handlers import user_router
from app.admin_handlers import admin_router
from config import TOKEN

#Асинхронная функция отправляющая на сервер тг запрос на сообщения
async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_routers(user_router, admin_router)
    await dp.start_polling(bot)


#Запуск асинхронной функции только через asyncio
#Конструкция IF позволяет запускать функцию main только из данного файла !!!
#logging логирование всех действий
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выкл')