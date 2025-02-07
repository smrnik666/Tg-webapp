from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from aiogram.utils import executor

TOKEN = "7912670623:AAFyieMi9tWxldMGIc6g3h291B39ICSAd_U"
WEB_APP_URL = "https://smrnik666.github.io/Tg-webapp/"  # Сюда вставляем URL веб-приложения

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Кнопка для открытия Web App
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton("Открыть каталог", web_app=WebAppInfo(url=WEB_APP_URL)))

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Привет! Нажми на кнопку, чтобы открыть каталог одежды.", reply_markup=keyboard)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
