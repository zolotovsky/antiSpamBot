import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.exceptions import TelegramBadRequest

# Включаем логирование (чтобы видеть ошибки)
logging.basicConfig(level=logging.INFO)

# Вставь сюда свой токен
TOKEN = "8154518874:AAGrkLYlLq5f4ZQEJXLQ1LlswqsLLd4lOG4"

# Создаём объект бота и диспетчер
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Список стоп-слов
STOP_WORDS = ["спам", "реклама", "лохотрон", "обман", "скам", "мошенник", "удаленная", "удаленка", "приглашаю", "заработок", "", "скам", "скам", "скам", "скам", "скам"]

# Фильтр сообщений (обрабатывает только текст)
@dp.message()
async def check_message(message: Message):
    # Проверяем, есть ли текст в сообщении
    if not message.text:
        return

    # Проверяем текст на стоп-слова
    for word in STOP_WORDS:
        if word.lower() in message.text.lower():
            try:
                await message.delete()
                
            except TelegramBadRequest:
                logging.warning(f"Не удалось удалить сообщение в чате {message.chat.id}")
            return

# Функция запуска бота
async def main():
    print("✅ Бот запущен и работает!")
    await dp.start_polling(bot)

# Запускаем бота
if __name__ == "__main__":
    asyncio.run(main())

import os
import asyncio
from aiohttp import web

# Функция для обработки HTTP-запросов (пинг от UptimeRobot)
async def handle(request):
    return web.Response(text="Bot is running!")

# Запуск веб-сервера
async def run_webserver():
    app = web.Application()
    app.router.add_get("/", handle)
    runner = web.AppRunner(app)
    await runner.setup()

    # Получаем порт от Render
    port = int(os.getenv("PORT", 8080))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()

# Добавляем веб-сервер в asyncio
async def main():
    asyncio.create_task(run_webserver())  # Запускаем веб-сервер
    print("✅ Web server is running to prevent Render from sleeping")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

