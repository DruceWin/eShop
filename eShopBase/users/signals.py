from django.dispatch import Signal

# A new user has registered.
# Provided args: user, request
user_registered = Signal()

# A user has activated his or her account.
# Provided args: user, request
user_activated = Signal()

#
# from django.core.mail import send_mail
# from django.db.models.signals import post_save
# from django.dispatch import receiver
#
# from .models import CustomUser
#
#
# @receiver(post_save, sender=CustomUser)
# def mail_send(sender, **kwargs):
#     # send_mail('Django',
#     #           f"Привет {kwargs['instance'].__dict__['username']}. Ты зарегистрирован(а) :)",
#     #           'djangoprojecteshop@mail.ru',
#     #           [kwargs['instance'].__dict__['email']],
#     #           fail_silently=True)
#     print('Регистрация в eShop',
#               f"Здраствуйте {kwargs['instance'].__dict__['username']}."
#               f"Для подтверждения регистрации в eShop перейдите по следующей ссылке: ___"
#               f"Если это были не вы, то просто удалите сообщение.",
#               'djangoprojecteshop@mail.ru',
#               [kwargs['instance'].__dict__['email']])
