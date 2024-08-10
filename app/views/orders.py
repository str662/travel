from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator
from core.custum_permission import LoggedSuperUser
from ..models import BuyModel

class OrderView(LoggedSuperUser, View):
    def get(self, request):
        order_list = BuyModel.objects.all().order_by('-id')
        paginator = Paginator(order_list, 15)  # 15 заказов на страницу

        page_number = request.GET.get('page')  # Получаем номер страницы из GET-запроса
        order = paginator.get_page(page_number)  # Получаем объект текущей страницы

        context = {
            'order': order  # Сохраняем имя переменной 'order' для пагинированного списка
        }
        return render(request=request, template_name='admin/orders.html', context=context)
