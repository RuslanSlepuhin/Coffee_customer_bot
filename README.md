# Customer bot

### *1. Return the user subscriber status*
- GET ^/subscribe-status?customer_bot&user_id=<user_id>

### *2. Get the order status from horeca throw server*
- POST ^/provide_message_to_user/
>{ \
> "user_id": int, \
> "order_id": str \
> "horeca_id": str \
> }

### *3. User verification*
- POST ^/verification/
>{ \
> "code": str, \
> }

Response:
> { \
> "code": str, \
> "user_id": int \
> }

How it works

1. Пользователь платит на сайте и ему предлагается отслеживать заказ в тг боте
   1. Проверка есть ли в ДБ user_id
      1. Есть -> Проверяем не заблокирован ли бот \
      \
      from backserver 
      > request \
      {"request": "is bot blocked"} 
      
      > response: \
      {"is bot blocked": [True or False]}

         1. Заблокирован -> предлагаем перейти в бот и стартовать
         2. Не заблокирован -> начинаем работу в боте с пользователем
         3. Нет -> даем ему верификацилонный сгенерированный код и кнопку в бот с инструкциями. Пользователь переходит 
      в бот, вводит код и начинаем работу в боте с пользователем
   
   3. Начинаем работу в боте с пользователем
      1. Интерфейс пользователя: кноппка отмена с описанием, что отменить можно будет до момента готовности заказа
      2. Бот получает и отображает изменения статусов. Как только приходит статус Готово, кнопка отменить пропадает

   4. Бот HoReCa
      1. Кабинет с мультивыбором диалога с пользователями
      2. 

Логика 
1) Пользователь на сайте оплачивает кофе:
   1) Если он уже авторизирован в customer боте, его telegram_user_id есть в базе  
      Нужно только проверить не заблокировал ли пользователь бота.   
      Сервер отправляет на эндппоинт get запрос и получает ответ False, если customer бот заблокирован пользователем и True, если пользователь подписан на customer bot  
      > GET ^/subscribe-status/

      Если True -> кнопка перейти в бота  
      Если False -> кнопка перейти в бота (вместе со /start)



   2) Если он не аторизован в боте, то его telegram_user_id нет в базе
      В таком случае ему генерируется верификационный код и предлагается через кнопку зайти в бот и ввести этот код  
      Как только ползователь вводит код, из бота отправляется POST запрос на энпоинт
      > POST ^/enter_key_from_user/  
      {  
      "teleram_user_id": int,  
      "verification_code": str  
      }
      

Сценарий 1:
Пользователь нажимает старт, вводит верификационный номер и пара приходит на сервер