from django.shortcuts import render
from django.views.generic.base import TemplateView
from resume.models import Resume


class ResumesView(TemplateView):
    template_name = 'resume/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'resumes': Resume.objects.all()})
