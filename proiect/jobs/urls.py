from django.urls import path

from jobs import views

app_name = 'jobs'

urlpatterns = [
    path('', views.JobView.as_view(), name='lista_joburi'),
    path('adaugare/', views.CreateJobView.as_view(), name="adaugare"),
    path('<int:pk>/update/', views.UpdateJobView.as_view(), name='modificare'),

    path('<int:pk>/delete/', views.delete_job, name='stergere'),
    path('<int:pk>/activate/', views.activate_job, name='activare'),
]