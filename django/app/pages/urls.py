from django.urls import path
from django.views.generic.base import RedirectView

from . import views

app_name = 'pages'
urlpatterns = [
    path('', RedirectView.as_view(pattern_name='hivernants:home', permanent=False), name='go-to-hivernants'),
]