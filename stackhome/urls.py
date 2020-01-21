from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from stackhome import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('apartments/', views.ApartmentList.as_view()),
    path('apartments/<int:pk>/', views.ApartmentDetail.as_view()),
    path('apartments/<int:pk>/rent', views.NewRent.as_view()),

    path('register/', views.UserRegister.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/me/', views.single_user),
    path('users/<int:pk>/', views.UserDetail.as_view()),

    path('apartments/me/', views.MyApartments.as_view()),
    path('apartments/add/', views.ApartmentAdd.as_view()),


    path('rooms/', views.RoomList.as_view()),
    path('rooms/<int:pk>/', views.RoomDetail.as_view()),
    path('rooms/me/', views.MyRooms.as_view()),
    path('rooms/add/', views.RoomAdd.as_view()),

    path('rents', views.RentsView.as_view()),

    path('token/', obtain_auth_token, name='api_token_auth'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
