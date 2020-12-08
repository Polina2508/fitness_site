from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
from .models import Reviews
from .forms import ReviewForm




class AddReview(View):

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
        return redirect('/')
        
        