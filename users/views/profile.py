from django.shortcuts import render
from django.views import View
from core.custum_permission import LoggedSuperUser


class ProfilePageView(View, LoggedSuperUser):
    def get(self, request):
        return render(request=request, template_name='users/profile.html')