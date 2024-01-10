Quick start

You have to use SQLite or PostgreSQL

1) git clone url
2) cd Coffee_customer_bot
3) pip install requirements
4) python -m main

For bot correct working your database must be not empty  

## Horeca bot
Bot get orders pull and show it in separate messages with buttons when you click 'start'.

### <u>Request from horeca bot [GET]:</u> 
> base url/client/horeca_info?telegram_horeca_id={user_id}&active=true
###### where user_id - barista telergam_user_id

Return:
```
{
    "response": [
        {
            "bot_subscribing": null,
            "enter_key": "44fdg",
            "horeca_id": 1,
            "id": 1,
            "order_description": "Ристретто без кофеина с добавлением воды",
            "order_id": "order1",
            "status": "placed",
            "telegram_horeca_id": 5884559465,
            "telegram_user_id": 5884559465
        },
        {
            "bot_subscribing": null,
            "enter_key": "motherfucker02",
            "horeca_id": 2,
            "id": 2,
            "order_description": "Вино Осеннее с добавлением кофеина. В одарок малосольный огурчик Боря",
            "order_id": "order2",
            "status": "in_progress",
            "telegram_horeca_id": 5884559465,
            "telegram_user_id": 5884559465
        },
        {
            "bot_subscribing": null,
            "enter_key": "44fdg",
            "horeca_id": 1,
            "id": 3,
            "order_description": "Мокаччино по итальянски. Делает итальянский повар с волосатой грудью",
            "order_id": "order3",
            "status": "ready",
            "telegram_horeca_id": 5884559465,
            "telegram_user_id": 5884559465
        }
    ]
}
```


A barista can to manage each order by status or cancelling it.
Each action send request to server endpoint to change the order status and server have to provide it to user

### <u>Request to change the order status [POST]:</u>
> base url/client/status_from_horeca/<str:order_id>/
###### where order_id -> the status updated order id 
```
{
    "bot_subscribing": "None", 
    "enter_key": "motherfucker02", 
    "horeca_id": 2, 
    "id": 2, 
    "order_description": "Вино Осеннее с добавлением кофеина. В одарок малосольный огурчик Боря", 
    "order_id": "order2", 
    "status": "ready", 
    "telegram_horeca_id": 5884559465, 
    "telegram_user_id": 5884559465
    }
```

Server sends json with changed status to other side (to the customer bot)
### <u>Request from the server to the customer bot [POST]:</u>
> base url/client/provide_message_to_user
```
{
    "bot_subscribing": "None", 
    "enter_key": "motherfucker02", 
    "horeca_id": 2, 
    "id": 2, 
    "order_description": "Вино Осеннее с добавлением кофеина. В одарок малосольный огурчик Боря", 
    "order_id": "order2", 
    "status": "ready", 
    "telegram_horeca_id": 5884559465, 
    "telegram_user_id": 5884559465
    }
```
The customer bot shows a notification about changing order status