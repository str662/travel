from django.shortcuts import render
from django.views import View
from core.custum_permission import LoggedSuperUser

from ..models import BuyModel

class OrderDetailView(LoggedSuperUser, View):
    def get(self, request, pk):
        try:
            order = BuyModel.objects.get(pk=pk) 
        except BuyModel.DoesNotExist:
            order = None 

        context = {
            'order': order
        }
        return render(request=request, template_name='admin/order_detail.html', context=context)
