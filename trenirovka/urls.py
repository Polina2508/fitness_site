from django.urls import path
from . import views
from .views import AddDesired

urlpatterns = [
    path("desired/", views.MoviesView.as_view(), name="movie_desired"),
    path("<int:pk>", views.AddDesired.as_view(),name="add_desired"),
]