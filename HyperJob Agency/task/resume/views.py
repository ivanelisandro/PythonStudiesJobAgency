from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from resume.models import Resume


class ResumesView(TemplateView):
    template_name = 'resume/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'resumes': Resume.objects.all()})


class CreateResumeView(TemplateView):
    template_name = 'resume/new.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, self.template_name)

        return HttpResponseForbidden(status=403)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            description = request.POST.get('description')
            resume = Resume(description=description, author=request.user)
            resume.save()
            return redirect('/home')

        return HttpResponseForbidden(status=403)
