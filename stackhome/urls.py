from django.urls import path
from stackhome import views

urlpatterns = [
    path('apartments/', views.apartment_list),
    path('apartments/<int:pk>/', views.apartment_detail)
]