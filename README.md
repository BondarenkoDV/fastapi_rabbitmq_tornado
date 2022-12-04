# fastapi_rabbitmq_tornado

Имеется форма с валидацией данных на Frontend, что бы в дальнейшем, Backend на Tornado обработал запрос и отправил его в сервис очередей RabbitMQ.  
Далее сервис на FastAPI принимает сообщение из сервиса очередей RabbitMQ и записывает их в PostgreSQL с помощью sqlalchemy.
