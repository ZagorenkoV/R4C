from django.core.mail import send_mail
from django.conf import settings

from robots.models import Robot
from orders.models import Order

from celery import Celery, shared_task
from celery.schedules import crontab

celery_app = Celery('tasks', broker='redis://localhost:6379/0')

@celery_app.shared_task
def process_robot_order(order_id):
    # Берет заказ из базы данных Order
    order = Order.objects.get(id=order_id)

    # проверяет, есть ли в наличии робот по базе данных Robot
    try:
        robot = Robot.objects.get(serial=order.robot_serial)
        # Если робот в наличии, отправляет письмо пользователю
        send_mail(
            'Ваш заказ был принят',
            f'Добрый день!\n Мы получили ваш заказ, {robot} в наличии на складе. Он будет доставлен в течение двух дней.',
            settings.DEFAULT_FROM_EMAIL,
            [order.customer],
            fail_silently=False,
        )
    except Robot.DoesNotExist:
        # Запускает фоновую задачу, которая проверяет раз в день появился ли робот в наличии
        check_robot_availability.apply_async((order.robot_serial, order.customer), countdown=1*24*60*60) #почитать проверить про эту таску, повторяется ли она каждый день countdown (возможно есть ретрай), 

@celery_app.shared_task
def check_robot_availability(robot_serial, customer_email):
    try:
        robot = Robot.objects.get(serial=robot_serial)
        # Если появился, отправляем письмо
        send_mail(
            'Your robot is now available',
            f'Добрый день!\n Недавно вы интересовались нашим роботом модели {robot.model}, версии {robot.version}. Этот робот теперь в наличии. Если вам подходит этот вариант - пожалуйста, свяжитесь с нами',
            settings.DEFAULT_FROM_EMAIL,
            [customer_email],
            fail_silently=False,
        )
    except Robot.DoesNotExist:
        pass

@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(crontab(hour='*/23'), check_robot_availability())