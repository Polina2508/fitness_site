from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect



def stretching_page(request):
    
    return render(request, template_name="stretching.html", context={})