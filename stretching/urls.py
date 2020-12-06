from django.urls import path
from stretching.views import stretching_page




urlpatterns = [
    path("", stretching_page, name="stretching_page"),

]