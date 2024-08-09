from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy

from core.custum_permission import LoggedSuperUser


class UserLogoutView(LogoutView, LoggedSuperUser):
    next_page = reverse_lazy('home_page')
