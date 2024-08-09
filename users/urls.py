from django.urls import path
from django.contrib.auth import views as auth_views

from .views import ProfilePageView, RegisterView, UserLoginView,\
UserLogoutView, ProfileUpdateView


urlpatterns = [
     path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('profile/', ProfilePageView.as_view(), name='profile'),
    path('regiter/', RegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/edit/', ProfileUpdateView.as_view(), name='profile_edit'),
]
