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
