from django.views.generic import DeleteView
from django.urls import reverse_lazy

from core.custum_permission import LoggedSuperUser
from ..models import ProductModel



class TourDeleteVeiw(LoggedSuperUser, DeleteView):
    model = ProductModel
    template_name = 'admin/delete_tour.html'
    success_url = reverse_lazy('home_page')