from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class MyPhoneBackend(ModelBackend):
    """
    Кастомный бэкэнд для авторизации через номер телефона
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get(UserModel.phone)
        if username is None or password is None:
            return
        try:
            user = UserModel.objects.get(phone=username)
        except UserModel.DoesNotExist:
            UserModel().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
