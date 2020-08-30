from django.urls import path, include
from . import views

app_name = 'page'

urlpatterns = [
    path('', views.index, name='result'),
    path('result/<str:movie>/', views.result, name='result'),
]
