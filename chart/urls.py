from django.urls import path

from chart import views

app_name = 'chart'

urlpatterns = [
    path('', views.index, name='index'),
]