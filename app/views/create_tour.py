from django.views.generic import CreateView
from django.urls import reverse_lazy
from core.custum_permission import LoggedSuperUser

from ..models import ProductModel, InExCludeModel


class TourCreateVeiw(LoggedSuperUser, CreateView):
    model = ProductModel
    fields = ['title', 'slug', 'about', 'prise', 'days', 'addres', 'image', 'exclude', 'include', 'start_date', 'end_date', 'country']
    template_name = 'admin/create_tour.html'
    success_url = reverse_lazy('home_page')
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class InExcludeViev(LoggedSuperUser, CreateView):

    model = InExCludeModel
    fields = ['name']
    template_name = 'admin/create_inrxcluda.html'
    success_url = reverse_lazy('super-admin')
