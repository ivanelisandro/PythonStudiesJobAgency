from django.shortcuts import render
from django.views.generic.base import TemplateView
from vacancy.models import Vacancy


class VacanciesView(TemplateView):
    template_name = 'vacancy/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'vacancies': Vacancy.objects.all()})
