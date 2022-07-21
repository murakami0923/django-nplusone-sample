from django.urls import path
from .views import (
    PersonListView001,
    PersonListView002
)

urlpatterns = [
    path('001/', PersonListView001.as_view()),
    path('002/', PersonListView002.as_view()),
]
