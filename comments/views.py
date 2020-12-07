from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View


class AddReview(View):

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        trenya = User.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.trenya = trenya
            form.save() 
        return redirect(trenya.get_absolute_url("/"))
        
        