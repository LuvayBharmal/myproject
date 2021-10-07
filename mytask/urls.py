from django.urls import path
from .views import GetLangugeData

urlpatterns = [
    path('language/',GetLangugeData.as_view(),name="myapi"),
]



