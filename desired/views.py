# from django.shortcuts import render
# from .models import Desired, Trenirovka
# from django.views.generic.base import View
# from django.shortcuts import redirect



# class TrenirovkaViewDesired(View):
    
#     def get(self, request):
#         trenirovka = request.user.desired.all()
#         return render(request, template_name="desired.html", context={"trenirovka":trenirovka})


# class AddDesired(View):

#     def post(self, request, pk):
#         trenirovka = Trenirovka.objects.get(id=pk)
#         Desired.objects.create(user=request.user, trenirovka=trenirovka)
#         return redirect('desired/')
