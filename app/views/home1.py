from django.shortcuts import render
from django.views import View

from ..models import ProductModel


class Home1View(View):
    def get(self, request):
        tours = ProductModel.objects.all()
        tours1 = ProductModel.objects.all().order_by('-publish_time')[:6]

        context={
            'tours' : tours,
            'tours1' : tours1
        }
        return render(request=request, template_name='home1.html', context=context)
