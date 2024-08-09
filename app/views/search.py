from django.views.generic import ListView
from datetime import datetime
from core.custum_permission import LoggedSuperUser

from ..models import ProductModel


class SearchResultView(ListView, LoggedSuperUser):
    model = ProductModel
    template_name = 'search.html'
    context_object_name = 'search_list'

    def get_queryset(self):
        query_params = self.request.GET
        
        country = query_params.get('country', '')
        start_date = query_params.get('start_date', '')
        min_price = query_params.get('min_price', 0)
        max_price = query_params.get('max_price', 10000000)
        
        queryset = ProductModel.objects.all()
        
        if country:
            queryset = queryset.filter(country__icontains=country)
        
        if start_date:
            try:
                start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
                queryset = queryset.filter(start_date__lte=start_date, end_date__gte=start_date)
            except ValueError:
                pass 
        
        if min_price and max_price:
            queryset = queryset.filter(prise__gte=min_price, prise__lte=max_price)
        
        return queryset

