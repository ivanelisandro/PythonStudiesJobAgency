from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from vacancy.models import Vacancy


class VacanciesView(TemplateView):
    template_name = 'vacancy/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'vacancies': Vacancy.objects.all()})


class CreateVacancyView(TemplateView):
    template_name = 'vacancy/new.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_staff:
            return render(request, self.template_name)

        return HttpResponseForbidden(status=403)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_staff:
            description = request.POST.get('description')
            vacancy = Vacancy(description=description, author=request.user)
            vacancy.save()
            return redirect('/home')

        return HttpResponseForbidden(status=403)
