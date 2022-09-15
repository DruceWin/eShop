from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django_registration.views import ActivationView, RegistrationView

from .forms import CustomUserRegisterForm, ChangeProfileForm, CustomLoginForm
from .models import CustomUser
import django.dispatch

profile = django.dispatch.Signal()


class CustomLoginView(LoginView):
    template_name = "login.html"
    form_class = CustomLoginForm


class CustomLogoutView(LogoutView):
    template_name = 'basePage.html'


class RegisterCustomUserView(CreateView):
    model = CustomUser
    template_name = 'register_form.html'
    form_class = CustomUserRegisterForm
    success_url = reverse_lazy('users:login')


def get_profile(request):
    profile.send(sender=get_profile)
    return render(request, "profile.html")


class ChangeProfile(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = CustomUser
    template_name = 'change_profile.html'
    form_class = ChangeProfileForm
    success_url = reverse_lazy('users:profile')
    success_message = 'Данные пользователя изменены'

    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().setup(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)


class PasswordChange(SuccessMessageMixin, LoginRequiredMixin, PasswordChangeView):
    template_name = 'change_password.html'
    success_url = reverse_lazy('users:profile')
    success_message = 'Пароль изменен'


class ActivationProfileView(ActivationView):
    pass


class RegistarionProfileView(RegistrationView):
    template_name = 'register_form.html'
    form_class = CustomUserRegisterForm
    success_url = reverse_lazy('users:login')

    def register(self, form):
        pass
