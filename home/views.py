from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
from .models import Reviews
from .forms import ReviewForm


# Create your views here.
def home_page(request):
    return render(request, template_name="home.html", context={})


class AddReview(View):

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
        return redirect('/')


class ReviewView(View):
    def get(self, request):
        review = Reviews.objects.all()
        return render(request, template_name="home.html", context={"review":review})

