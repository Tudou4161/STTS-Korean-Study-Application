from django.urls import path
from django.contrib import admin
from main_app import views

app_name = "main_app"

urlpatterns = [
    path('', views.main, name="main"),
    path('chapter/', views.chapter, name="chapter"),
    path('chapter/<int:cn_ChapNo>/chap_detail', views.chap_detail, name="chap_detail"),
    path('chapter/<int:cn_ChapNo>/chap_detail/chap_sentence', views.chap_sentence_ES, name="chap_Essential_sentence"),
    path('chapter/<int:cn_ChapNo>/chap_detail/chap_sentence2', views.chap_sentence_Con, name="chap_conversation_sentence"),
    path('chapter/<int:cn_ChapNo>/chap_detail/chap_sentence/LV1clear', views.LV1clear, name="LV1clear"),
]