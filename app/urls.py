from django.urls import path

from .views import Home1View, AboutView, TourView, ContactView, TourDetailView,\
SearchResultView, TourCreateVeiw, AdminView, TourDeleteVeiw


urlpatterns = [
    path('', Home1View.as_view(), name='home_page'),
    path('about/', AboutView.as_view(), name='about_page'),
    path('tour/', TourView.as_view(), name='tour_page'),
    path('contact/', ContactView.as_view(), name='contact_page'),
    path('tour_detail/<slug:slug>/', TourDetailView.as_view(), name='tour_detail_page'),
    path('search/', SearchResultView.as_view(), name='search_page'),
    path('create-tour/', TourCreateVeiw.as_view(),name='tour_create'),
    path('tour_detail/<slug>/delete', TourDeleteVeiw.as_view(), name='delete-tour'),
    path('super-admin/', AdminView.as_view(), name='super-admin')
]
