from django.urls import path
from .views import GetLanguageDetails

urlpatterns = [
    path('language/<language>/<word>/', GetLanguageDetails.as_view() , name="myapi"),
]



