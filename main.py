from aiogram import Bot, Dispatcher, types, executor
import pyqrcode

bot = Bot(token='5946619198:AAFaXgfll5NQYsdfctnGSDjVHREL7AlP-xg')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    full_name = message.from_user.full_name
    await message.reply(f"Hello 🖐🏼{full_name},send me anything ")


@dp.message_handler(commands=['logo'])
async def logo_handler(message: types.Message):
    await message.answer_photo('https://github.com/settings/profile')


@dp.message_handler()
async def qr(message: types.Message):
    text = pyqrcode.create(message.text)
    text.png('code.png', scale=5)
    await bot.send_photo(chat_id=message.chat.id, photo=open('code.png', 'rb'))


if __name__ == '__main__':
    print('My Bot is successful')
    executor.start_polling(dp, skip_updates=True)
