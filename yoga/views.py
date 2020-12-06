from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect



def yoga_page(request):
    
    return render(request, template_name="yoga.html", context={})