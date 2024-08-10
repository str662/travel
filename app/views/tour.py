from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from ..models import ProductModel


class TourView(View):
    def get(self, request):
        tour_list = ProductModel.objects.all()
        paginator = Paginator(tour_list, 6)
        page = request.GET.get('page')

        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)

        context = {
            'products': products,
        }
        return render(request=request, template_name='tour.html', context=context)