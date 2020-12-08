from django.urls import path
from comments.views import AddReview
from . import views




urlpatterns = [
    path('', views.AddReview.as_view(), name='add_review'),
]