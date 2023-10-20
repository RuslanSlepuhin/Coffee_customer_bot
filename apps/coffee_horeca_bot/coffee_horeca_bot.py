from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor

class HorecaBot:
    # print('HorecaBot has been started\nhttps://t.me/medicine_card_bot\n')

    def __init__(self, token):
        self.token = token
        self.bot = Bot(token=token)
        self.dp = Dispatcher(self.bot, storage=MemoryStorage())

    def bot_handlers(self):

        @self.dp.message_handler(commands=['get_users'])
        async def get_users(message: types.Message):
            pass

        @self.dp.message_handler(commands=['start'])
        async def start(message: types.Message):
            pass

        @self.dp.callback_query_handler()
        async def callbacks(callback: types.CallbackQuery):
            pass

        @self.dp.message_handler(content_types=['text'])
        async def text_message(message):
            pass

        executor.start_polling(self.dp, skip_updates=True)
