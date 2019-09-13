from django.urls import path
from stackhome import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('apartments/', views.ApartmentList.as_view()),
    path('apartments/<int:pk>/', views.ApartmentDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)