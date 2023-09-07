from django.urls import path
from . import views
from .views import HomeView, PostDetail

#urlpatterns = [
#    path('boooking.urls/', views.booking_reservation, name='booking_reservation'),
    # Add more URL patterns here as needed
#]

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('bookings/', views.PostDetail.as_view(), name='booking_list'),
    path('bookings/<int:pk>/', views.EditBooking.as_view(), name='edit-booking'),
]