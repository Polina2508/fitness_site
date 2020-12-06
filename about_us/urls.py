from django.urls import path
from about_us.views import about_us_page




urlpatterns = [
    path("", about_us_page, name="about_us_page"),

]
