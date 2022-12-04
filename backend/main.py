import os
import asyncio
import tornado.ioloop
import tornado.web
import tornado.template
from tornado.options import options, define
import pika
import tornado.escape
import json


define("host", default="localhost", help="app host", type=str)
define("port", default=8888, help="Запущено на установленном порте", type=int)
define("debug", default=True, help="Запущено в debug mode")


class MainPage(tornado.web.RequestHandler):

    def get(self):
        self.render("index.html")

    def post(self):
        data = self.request.arguments
        last_name = data['last_name'][0].decode("utf-8")
        first_name =  data['first_name'][0].decode("utf-8")   
        patronymic =  data['patronymic'][0].decode("utf-8")
        phone =  data['phone'][0].decode("utf-8")
        message =  data['message'][0].decode("utf-8")
        data = {
            'last_name': last_name,
            'first_name': first_name,
            'patronymic': patronymic,
            'phone': phone,
            'message': message,
        }
        connection = pika.BlockingConnection(
            pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        message = ''.join(json.dumps(data, ensure_ascii=False))
        channel.basic_publish(
            exchange='',
            routing_key='task_queue',
            body=message,
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ))

        print(" [x] Sent %r" % message)
        channel.connection.close()


async def main():
    app = tornado.web.Application(
        [
            (r"/", MainPage),
        ],
        web_title="Отправка формы",
        template_path=os.path.join(os.path.abspath("frontend"), "templates"),
        static_path=os.path.join(os.path.abspath("frontend"), "static"),
        debug=options.debug,
    )
    app.listen(options.port)
    await asyncio.Event().wait()


if __name__ == "__main__":
    try:
        print('Tornado server is starting...')
        asyncio.run(main())
    except KeyboardInterrupt:
        print('\nTornado server is stopped')
        exit(0)
