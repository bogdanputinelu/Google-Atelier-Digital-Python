from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView

from jobs.models import Job


# Create your views here.
class JobView(LoginRequiredMixin, ListView):
    model = Job
    template_name = 'jobs/job_index.html'


class CreateJobView(LoginRequiredMixin, CreateView):
    model = Job
    fields = ['job_type', 'title', 'url', 'description']
    template_name = 'jobs/job_form.html'

    def get_success_url(self):
        return reverse('jobs:lista_joburi')


class UpdateJobView(LoginRequiredMixin, UpdateView):
    model = Job
    fields = ['job_type', 'title', 'url', 'description']
    template_name = 'jobs/job_form.html'

    def get_success_url(self):
        return  reverse('jobs:lista_joburi')


@login_required
def delete_job(request, pk):
    Job.objects.filter(id=pk).update(active=0)
    return redirect('jobs:lista_joburi')


@login_required
def activate_job(request, pk):
    Job.objects.filter(id=pk).update(active=1)
    return redirect('jobs:lista_joburi')