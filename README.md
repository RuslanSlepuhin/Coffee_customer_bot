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

