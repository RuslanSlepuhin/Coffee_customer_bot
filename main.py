import configparser
from apps.coffee_customer_bot.coffee_customer_bot import CustomerBot
from apps.coffee_horeca_bot.coffee_horeca_bot import HorecaBot
from multiprocessing import Process
from apps.endpoints.endpoints import Endpoints

config = configparser.ConfigParser()
config.read('./apps/settings/config.ini')

customer_token = config['Bot']['customer_token']
horeca_token = config['Bot']['horeca_token']

def start_customer_bot(token):
    customer_bot = CustomerBot(token)
    customer_bot.bot_handlers()

def start_horeca_bot(token):
    horeca_bot = HorecaBot(token)
    horeca_bot.bot_handlers()

def start_endpoints():
    endpoints = Endpoints()
    endpoints.main_endpoints()

if __name__ == '__main__':

    p1 = Process(target=start_customer_bot, args=(customer_token, ))
    p2 = Process(target=start_horeca_bot, args=(horeca_token, ))
    p3 = Process(target=start_endpoints, args=())

    p1.start()
    p2.start()
    p3.start()
