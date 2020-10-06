from django.urls import path
from . import views


urlpatterns=[
    path("", views.TaskView.as_view()),
    path("solve/<int:pk>/", views.SolveTask.as_view())
]