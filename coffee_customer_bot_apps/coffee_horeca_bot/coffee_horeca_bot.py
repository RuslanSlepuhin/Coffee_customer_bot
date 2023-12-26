import configparser
import json

import requests
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.utils import executor
from coffee_customer_bot_apps.variables import variables
from coffee_customer_bot_apps.coffee_horeca_bot.horeca_add_methods import HorecaBotMethods

config = configparser.ConfigParser()
config.read("./coffee_customer_bot_apps/settings/config.ini")

class HorecaBot:
    # print('HorecaBot has been started\nhttps://t.me/medicine_card_bot\n')

    def __init__(self, token=None):
        self.token = token if token else config['Bot']['horeca_token']
        self.bot = Bot(token=self.token)
        self.dp = Dispatcher(self.bot, storage=MemoryStorage())
        self.user_data = {}
        self.messages_list = []
        self.status_number = 0
        self.message = None
        self.methods = HorecaBotMethods(self)

    def bot_handlers(self):

        @self.dp.message_handler(commands=['start'])
        async def start(message: types.Message):
            await self.bot.send_message(message.chat.id, f"Your id is {message.chat.id}")
            await self.methods.start(message)

        @self.dp.callback_query_handler()
        async def callbacks(callback: types.CallbackQuery):
            pass

        @self.dp.message_handler(content_types=['text'])
        async def text_message(message):

            self.user_data['telegram_user_id'] = message.chat.id
            self.user_data['status'] = message.text

            if message.text in variables.BARISTA_STATUS_CHOICES.values():
                print('send from bot')
                requests.post(f"{variables.server_domain}{variables.server_test_status_endpoint_from_horeca}",
                              json=self.user_data)
                print('sent from bot')
                await self.change_status(message)

            elif message.text in variables.BARISTA_NEGATIVE_STATUS_CHOICES.values():
                print('negative_status')
                requests.post(f"{variables.server_domain}{variables.server_test_status_endpoint_from_horeca}",
                              json=self.user_data)
                print('sent from bot')
                self.status_number = -1
                await self.change_status(message)


        executor.start_polling(self.dp, skip_updates=True)

    async def custom_send_message(self, data):
        self.user_data = data
        user_id = self.user_data['telegram_horeca_id']
        await self.bot.send_message(user_id, str(self.user_data))

        # await self.bot.send_message(user_id, str(data['status']))
        pass

    async def check_subscriber(self, user_id):
        try:
            msg = await self.bot.send_message(int(user_id), "Вы можете отслеживать Ваш заказ в этом боте")
            await msg.delete()
            return True
        except:
            return False





