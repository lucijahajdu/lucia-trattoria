from django.urls import path
from . import views

#urlpatterns = [
#    path('boooking.urls/', views.booking_reservation, name='booking_reservation'),
    # Add more URL patterns here as needed
#]

urlpatterns = [
    path('bookings/', views.PostDetail.as_view(), name='booking_list'),
    path('bookings/<int:booking_id>/', views.booking_detail, name='booking_detail'),
]