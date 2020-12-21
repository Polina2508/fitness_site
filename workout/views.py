from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from trenirovka.models import Trenirovka
from django.views.generic.base import View
from trenirovka.models import Category


class MoviesView(View):
    def get(self, request): 
        stretching = Trenirovka.objects.filter(category = "1")
        return render(request, template_name="stretching.html", context={"stretching":stretching})

class MoviesView1(View):
    def get(self, request):
        yoga = Trenirovka.objects.filter(category = "2")
        return render(request, template_name="yoga.html", context={"yoga":yoga})

class MoviesView2(View):
    def get(self, request):
        sila = Trenirovka.objects.filter(category = "3")
        return render(request, template_name="sila.html", context={"sila":sila})

# def stretching_page(request):
#     return render(request, template_name="stretching.html", context={})
def work_page(request):
    return render(request, template_name="workout.html", context={})