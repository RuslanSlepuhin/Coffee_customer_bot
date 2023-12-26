import json

import requests
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

from coffee_customer_bot_apps.variables import variables


class HorecaBotMethods:

    def __init__(self, main_class):
        self.main_class = main_class

    async def get_user_data(self, message):
        if not self.main_class.user_data:
            url = variables.server_domain + variables.get_horeca_info + f"?telegram_horeca_id={message.chat.id}"
            self.main_class.user_data = requests.get(url)
            self.main_class.user_data = json.loads(self.main_class.user_data.content.decode('utf-8'))

    async def start(self, message):
        print(message.chat.id)
        await self.get_user_data(message)
        await self.change_status(message)

    async def change_status(self, message):
        if self.main_class.status_number >= 0:
            button_value_list = []
            keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
            key = list(variables.BARISTA_STATUS_CHOICES.keys())[self.main_class.status_number]
            button_value_list.append(KeyboardButton(variables.BARISTA_STATUS_CHOICES[key]))

            if key == "in_progress":
                button_value_list.append(KeyboardButton(variables.BARISTA_NEGATIVE_STATUS_CHOICES['canceled_by_cafe']))
            if key == "delivered":
                button_value_list.append(KeyboardButton(variables.BARISTA_NEGATIVE_STATUS_CHOICES['utilized']))

            keyboard.add(*button_value_list)

            self.message = await self.main_class.bot.send_message(message.chat.id, "Изменить статус", reply_markup=keyboard)

            if self.status_number < len(variables.BARISTA_STATUS_CHOICES.keys()) - 1:
                self.status_number += 1
            else:
                self.status_number = -1
        else:
            await self.main_class.bot.send_message(message.chat.id, f"Заказ №{self.main_class.user_data['order_id']} закрыт", reply_markup=ReplyKeyboardRemove())

