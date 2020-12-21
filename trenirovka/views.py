from django.shortcuts import render
from .models import Trenirovka
from desired.models import Desired
from django.views.generic.base import View
from django.shortcuts import redirect
from .models import Category
from django.db.models import Q
 



class MoviesView(Category, View):
    def get(self, request):
        trenirovka = Trenirovka.objects.all()
        return render(request, template_name="desired.html", context={"trenirovka":trenirovka})

# class TrenirovkaViewDesired(View):
    
#     def get(self, request):
#         trenirovka = request.user.desired.all()
#         return render(request, template_name="desired.html", context={"trenirovka":trenirovka})


class AddDesired(View):

    def post(self, request, pk):
        trenirovka = Trenirovka.objects.get(id=pk)
        Desired.objects.create(user=request.user, name=trenirovka)
        return redirect('accounts/')
    
class Category:

    def get_category(self):
        return Category.objects.all().values("strething")