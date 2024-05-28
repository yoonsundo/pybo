from django.urls import path

from exam import views

app_name = 'exam'

urlpatterns = [
    path('', views.index, name='index'),
    path('findExamList', views.findExamList, name='findExamList'),
]