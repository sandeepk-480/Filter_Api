from django.urls import path
from app.views import DataList


urlpatterns = [
    path('Api/', DataList.as_view()),
]