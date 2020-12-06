from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from .models import Trenirovka


def work_page(request):
    treni = Trenirovka.objects.all()
    return render(request, template_name="workout.html", context={})


