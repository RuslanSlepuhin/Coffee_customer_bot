import configparser
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import requests
from aiogram.utils import executor
from coffee_customer_bot_apps.variables import variables

config = configparser.ConfigParser()
config.read("./coffee_customer_bot_apps/settings/config.ini")

class CustomerBot:
    def __init__(self, token=None):
        self.token = token if token else config['Bot']['customer_token']
        self.bot = Bot(token=self.token)
        self.dp = Dispatcher(self.bot, storage=MemoryStorage())
        self.test_data = {
            'id': 12365,
            'id_order': 14,
            'id_horeca': 12,
            'status': 'cancel'
        }

    def bot_handlers(self):

        @self.dp.message_handler(commands=['get_users'])
        async def get_users(message: types.Message):
            pass

        @self.dp.message_handler(commands=['start'])
        async def start(message: types.Message):
            keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = KeyboardButton("Отмена заказа")
            button2 = KeyboardButton("Верните бабло")
            keyboard.add(button1, button2)
            await self.bot.send_message(message.chat.id, "PRESS BUTTON", reply_markup=keyboard)
            pass

        @self.dp.callback_query_handler()
        async def callbacks(callback: types.CallbackQuery):
            pass

        @self.dp.message_handler(content_types=['text'])
        async def text_message(message):
            self.test_data['user_id'] = message.chat.id
            self.test_data['status'] = message.text

            if message.text == 'Отмена заказа':
                requests.post(f"http://127.0.0.1:5000/{variables.server_test_status_endpoint_from_customer}",
                              json=self.test_data)
            elif message.text == "Верните бабло":
                requests.post(f"http://127.0.0.1:5000/{variables.server_test_status_endpoint_from_customer}",
                              json=self.test_data)


        executor.start_polling(self.dp, skip_updates=True)

    async def custom_send_message(self, data):
        user_id = data['user_id']
        await self.bot.send_message(user_id, str(data))