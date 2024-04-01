from django.shortcuts import render,redirect
from django.views.generic import View
from store.forms import RegForm



class RegView(View):
    def get(self, request, *args, **kwargs):
        form = RegForm()
        return render(request,"register.html", {'form': form})

    def post(self, request, *args, **kwargs):
        form = RegForm(request.POST)
        if form.is_valid():
            form.save()
            print("saved")
            return redirect("home")
        else:
            print("not saved")
            return render(request,"register.html", {'form': form})