from django.urls import path
from workout.views import work_page
from . import views




urlpatterns = [
    path("", work_page, name="work_page"),
    path("stretching/", views.MoviesView.as_view(), name="stretching_page"),
    path("yoga/", views.MoviesView1.as_view(), name="yoga_page"),
    path("sila/", views.MoviesView2.as_view(), name="sila_page"),
]

