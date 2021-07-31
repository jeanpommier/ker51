from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.template import loader
from django.views import generic
from django_tables2 import SingleTableView

from .models import Person
from .tables import PersonTable
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


class IndexView(SingleTableView):
    model = Person
    table_class = PersonTable
    # context_object_name = 'persons'
    template_name = 'map/index.html'

    # def get_queryset(self):
    #     return Person.objects.order_by('names')


class DetailView(generic.DetailView):
    model = Person
    template_name = 'map/detail.html'