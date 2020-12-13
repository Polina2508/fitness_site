from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect



def work_page(request):
    return render(request, template_name="workout.html", context={})


