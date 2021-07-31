from django.urls import path

from . import views

app_name = 'map'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('person/<int:pk>', views.DetailView.as_view(), name='detail'),
]