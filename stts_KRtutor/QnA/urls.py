from django.contrib import admin
from django.urls import path, include
from .views import *
from django.views.generic.detail import DetailView
from .models import QuestionAndAnswer

app_name = "QnA"

urlpatterns = [
    path('', QnA_list, name="QnA_list"),
    path('', MyQnA, name="MyQnA"),
    path('detail/<int:pk>/', DetailView.as_view(model=QuestionAndAnswer, template_name="QnA/detail.html"), name="QnA_detail"),
    path('upload/', QnAUploadView.as_view(), name="QnA_upload"),
    path('update/<int:pk>/', QnAUpdateView.as_view(), name="QnA_update"),
    path('delete/<int:pk>/', QnADeleteView.as_view(), name="QnA_delete"),
]
