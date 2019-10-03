from django.urls import path
from stackhome import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('apartments/', views.ApartmentList.as_view()),
    path('apartments/<int:pk>/', views.ApartmentDetail.as_view()),

    path('users/', views.UserList.as_view()),
    path('users/register', views.UserRegister.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),

    path('apartments/me/', views.MyApartments.as_view()),
    path('apartments/add/', views.ApartmentAdd.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
