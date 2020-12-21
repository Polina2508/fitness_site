from django.urls import path
from home.views import food_page
from home.views import home_page
from . import views




urlpatterns = [
    path("food/", food_page, name="food_page"),
    path('aa/', views.AddReview.as_view(), name='add_review'),
    path('', views.ReviewView.as_view(), name='review_review'),
    path("", home_page, name="home_page"),

]