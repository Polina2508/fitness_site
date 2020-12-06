from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect



def about_us_page(request):
    
    return render(request, template_name="about_us.html", context={})