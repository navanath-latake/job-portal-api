from django.urls import path
from .views import (
    ApplyView,
    MyApplicationsView,
    JobApplicationsView,
    ApplicationStatusView,
)

urlpatterns = [
    path('',                    ApplyView.as_view(),             name='apply'),
    path('my/',                 MyApplicationsView.as_view(),    name='my-applications'),
    path('job//',   JobApplicationsView.as_view(),   name='job-applications'),
    path('/status/',    ApplicationStatusView.as_view(), name='application-status'),
]