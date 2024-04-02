from django.views import generic
from django.http import HttpResponse
from . import models, rezka_parser, forms


class GetParsing(generic.FormView):
    template_name = "parsers/get_parsing.html"
    form_class = forms.ParserSiteForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse("<h1>Parsing...Successful</h1>")
        else:
            return super(GetParsing, self).post(request, *args, **kwargs)


class RezkaListView(generic.ListView):
    template_name = "parsers/rezka_list.html"
    model = models.RezkaParser
    context_object_name = "rezka"

    def get_queryset(self):
        return self.model.objects.all()


class ManasListView(generic.ListView):
    template_name = "parsers/manas_list.html"
    model = models.ManasParser
    context_object_name = "manas"

    def get_queryset(self):
        return self.model.objects.all()
