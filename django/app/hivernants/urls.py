from django.urls import path

from . import views

app_name = 'hivernants'
urlpatterns = [
    path('list', views.ListView.as_view(), name='list'),
    path('map', views.MapView.as_view(), name='map'),
    path('<int:pk>', views.DetailView.as_view(), name='detail'),
    path('', views.HomeView.as_view(), name='home'),
]