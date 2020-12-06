from django.urls import path
from workout.views import work_page




urlpatterns = [
    path("", work_page, name="work_page"),

]

