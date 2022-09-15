from django.urls import path
from django.views.generic.base import TemplateView

from .views import CustomLogoutView, RegisterCustomUserView, get_profile, ChangeProfile, \
    PasswordChange, CustomLoginView, RegistarionProfileView, ActivationProfileView

app_name = "users"

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', get_profile, name='profile'),
    path('register/', RegisterCustomUserView.as_view(), name='register'),
    path('change_profile/', ChangeProfile.as_view(), name='change_profile'),
    path('change_password/', PasswordChange.as_view(), name='change_password'),
    # path("activate/<str:activation_key>/", ActivationProfileView.as_view(), name="django_registration_activate"),
    # path("register/", RegistarionProfileView.as_view(), name="register"),
    # # path("register/", RegistarionProfileView.as_view(), name="django_registration_register"),
    # path("activate/complete/", TemplateView.as_view(template_name="activation_complete.html"),
    #      name="django_registration_activation_complete"),
    # path("register/complete/", TemplateView.as_view(template_name="registration_complete.html"),
    #      name="django_registration_complete"),
    # path("register/closed/", TemplateView.as_view(template_name="registration_closed.html"),
    #      name="django_registration_disallowed"),
]
