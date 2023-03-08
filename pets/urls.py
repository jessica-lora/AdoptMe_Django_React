from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from pets import views

urlpatterns = [
    path('/', views.PetsList.as_view()),
    path('/<int:pk>/', views.PetDetail.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)