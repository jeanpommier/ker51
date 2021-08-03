import django_tables2 as tables
from django.utils.html import format_html
from .models import Hivernant

class HivernantTable(tables.Table):
    fulladdress = tables.TemplateColumn('{{ record.fulladdress|linebreaks }}')
    comments = tables.TemplateColumn('{{ record.comments|linebreaks }}')
    phones = tables.Column(empty_values=())
    emails = tables.Column(empty_values=())

    def render_picture(self, value, record):
        return format_html('<img src="{}" alt="{}" title="{}" class="picture_small"/>', value.url, record.names, record.names)

    def render_phones(self, record):
        p = '<br />'.join([ phone.__str__() for phone in record.phone_set.all() ])
        return format_html(p)

    def render_emails(self, record):
        p = '<br />'.join([ email.__str__() for email in record.email_set.all() ])
        return format_html(p)

    class Meta:
        model = Hivernant
        template_name = "django_tables2/bootstrap.html"
        fields = ('names', 'fulladdress', 'comments','picture',)
        attrs = {"class": "table liste_hivernants"}