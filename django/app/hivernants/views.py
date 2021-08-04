from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.template import loader

import json

from django.views import generic
from django_tables2 import SingleTableView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.serializers import serialize
from django.views.generic.base import TemplateView

from .models import Hivernant, Person
from .tables import HivernantTable
#
# def index(request):
#     persons = Person.objects.order_by('names')
#     context = {
#         'persons': persons,
#     }
#     return render(request, 'map/index.html', context)

# def detail(request, person_id):
#     person = get_object_or_404(Person, pk=person_id)
#     return render(request, 'map/detail.html', {'person': person})


class HomeView(TemplateView):
    template_name = 'hivernants/index.html'

class ListView(LoginRequiredMixin, SingleTableView):
    model = Hivernant
    table_class = HivernantTable
    # context_object_name = 'persons'
    template_name = 'hivernants/liste.html'

    # def get_queryset(self):
    #     return Person.objects.order_by('names')

class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Hivernant
    template_name = 'hivernants/detail.html'

class MapView(LoginRequiredMixin, generic.TemplateView):
    model = Hivernant
    template_name = 'hivernants/map.html'

    def get_context_data(self, **kwargs):
        """Return the view context data."""
        context = super().get_context_data(**kwargs)
        context["markers"] = json.loads(
            serialize("geojson",
                      Person.objects.all(),
                      geometry_field='location',
                      fields=('names', 'fulladdress', 'picture')
                      )
        )
        return context
