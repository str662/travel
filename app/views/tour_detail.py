from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from core.custum_permission import LoggedSuperUser
from ..models import ProductModel
from ..forms import BuyForm

class TourDetailView(View, LoggedSuperUser):
    def get(self, request, slug):
        tours = get_object_or_404(ProductModel, slug=slug)
        form = BuyForm(initial={'tour': tours.title, 'date': tours.start_date})
        context = {
            'tours': tours,
            'form': form,
        }
        return render(request, 'tour-details.html', context)

    def post(self, request, slug):
        tours = get_object_or_404(ProductModel, slug=slug)
        form = BuyForm(request.POST, tour_title=tours.title, start_date=tours.start_date)
        if form.is_valid():
            form.save()
            return redirect('home_page')
        context = {
            'form': form,
            'tours': tours
        }
        return render(request, 'tour-details.html', context)

