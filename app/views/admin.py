from django.shortcuts import render
from django.views import View

from core.custum_permission import LoggedSuperUser


class AdminView(LoggedSuperUser,View):
    def get(self, request):
        return render(request=request, template_name='admin/admin.html')