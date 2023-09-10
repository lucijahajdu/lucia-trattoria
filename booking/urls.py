from django.urls import path
from . import views
from .views import HomeView, PostDetail, EditBooking, DeleteBooking
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('bookings/', views.PostDetail.as_view(), name='booking_list'),
    path('bookings/<int:pk>/', EditBooking.as_view(), name='edit-booking'),
    path(
        'bookings/delete/<int:pk>/', DeleteBooking.as_view(),
        name='delete-booking'
        ),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]
