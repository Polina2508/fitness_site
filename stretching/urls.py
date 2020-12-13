from django.urls import path
# from stretching.views import stretching_page
from . import views




urlpatterns = [
    # path("", stretching_page, name="stretching_page"),
    path("", views.MoviesView.as_view(), name="stretching_page"),
]