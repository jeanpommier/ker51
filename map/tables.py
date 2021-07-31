import django_tables2 as tables
from .models import Person

class PersonTable(tables.Table):
    fulladdress = tables.TemplateColumn('{{ record.fulladdress|linebreaks }}')
    comments = tables.TemplateColumn('{{ record.comments|linebreaks }}')
    class Meta:
        model = Person
        template_name = "django_tables2/bootstrap.html"
        fields = ('names', 'fulladdress', 'phones', 'emails', 'comments',)