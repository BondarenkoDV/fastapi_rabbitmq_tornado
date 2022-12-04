import pika
from settings import settings
import uvicorn
from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session
import time
import sys
import os
import json
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from db import models, schemas
from db.database import engine, get_session

models.Base.metadata.create_all(engine)
app = FastAPI(version='0.1',
              title='Приложение',
              description='Тестовое приложение для "Ростелеком"')


@app.post("/f")
def send_to_db(session: Session = Depends(get_session)):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='task_queue', durable=True)
    method_frame, header_frame, body = channel.basic_get(
        'task_queue', auto_ack=True)
    if body is not None:
        data = json.loads(body)
        new = models.Feedback(
            first_name=data['first_name'],
            last_name=data['last_name'],
            patronymic=data['patronymic'],
            phone=data['phone'],
            message=data['message'],
        )
        session.add(new)
        session.commit()
    channel.stop_consuming()
    connection.close()
    return new


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.server_host,
        port=settings.server_port,
        reload=True,
    )
