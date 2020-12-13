from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from trenirovka.models import Trenirovka
from django.views.generic.base import View

class MoviesView(View):
    def get(self, request):
        trenirovka = Trenirovka.objects.all()
        return render(request, template_name="stretching.html", context={"trenirovka":trenirovka})

# def stretching_page(request):
#     return render(request, template_name="stretching.html", context={})