import datetime

from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from django.utils.deconstruct import deconstructible
from django.core import validators
from django_registration.forms import RegistrationForm

from .models import CustomUser


@deconstructible
class PhoneValidator(validators.RegexValidator):
    regex = r"^\+{1}\d{11}"
    message = "Введите реальный номер телефона."
    flags = 0


class CustomUserRegisterForm(forms.ModelForm):
    username = forms.CharField(required=True,
                               label='Имя пользователя',
                               max_length=30,
                               validators=[UnicodeUsernameValidator()])
    email = forms.EmailField(required=True,
                             label='Email')
    phone = forms.CharField(required=True,
                            label='Номер телефона',
                            max_length=13,
                            initial='+375',
                            validators=[PhoneValidator()],
                            help_text="Введите номер в международном формате +375YYXXXXXXX")
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput,
                                help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label='Повторите пароль',
                                widget=forms.PasswordInput)
    birthday = forms.DateField(label='Дата рождения',
                               widget=forms.SelectDateWidget(
                                   years=range(datetime.date.today().year - 150, datetime.date.today().year)))
    address = forms.CharField(label='Адрес')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-CustomUserRegisterForm'
        # self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'username',
            'email',
            'phone',
            'password1',
            'password2',
            'first_name',
            'last_name',
            Field('birthday', style='display:inline-flex; width: 33.33%'),
            'address')

        self.helper.add_input(Submit('submit', 'Зарегистрироваться', style='width: 100%; margin-top: 5;'))

    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        if password1:
            password_validation.validate_password(password1)
        return password1

    def clean(self):
        super().clean()
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            errors = {'password2': ValidationError(
                'Введенные пароли не совпадают', code='password_mismatch')}
            raise ValidationError(errors)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_active = True
        if commit:
            user.save()
        return user

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone', 'password1', 'password2', 'first_name', 'last_name', 'birthday',
                  'address']


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(label='Номер или email',
                               validators=[UnicodeUsernameValidator()])
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-CustomUserLoginForm'
        # self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'username',
            'password')

        self.helper.add_input(Submit('submit', 'Войти', style='width: 100%; margin-top: 5;'))


class ChangeProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['phone', 'first_name', 'last_name', 'address']

#
# class MyCustomUserForm(RegistrationForm):
#     class Meta(RegistrationForm.Meta):
#         model = CustomUser
