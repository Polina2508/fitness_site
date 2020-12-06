from django.urls import path
from yoga.views import yoga_page




urlpatterns = [
    path("", yoga_page, name="yoga_page"),

]
