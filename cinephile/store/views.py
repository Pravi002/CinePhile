from django.shortcuts import render,redirect
from django.views.generic import View,ListView
from store.forms import RegForm,LoginForm
from store.models import Movie,WatchList,Diary
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator


def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fn(request,*args,**kwargs)
        else:
            return redirect("login")
    return wrapper



class HomeView(View):
    def get(self,request,*args,**kwargs):
        form=Movie.objects.all()
        return render(request,"home.html",{"form":form})
 

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
        

class LoginView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            u_name=form.cleaned_data.get("username")
            pswd=form.cleaned_data.get("password")
            user_obj=authenticate(request,username=u_name,password=pswd)
            if user_obj:
                print("valid credential")
                login(request,user_obj)
                return redirect("home")
            else:
                print("invalid credential")
                return render(request,"login.html",{"form":form})
            

class LogoutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("home")
    
    

class MovieDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        data=Movie.objects.filter(id=id)
        return render(request,"movie_detail.html",{"data":data})



class MovieGenre(View):
    def get(self,request,*args,**kwargs):
        genre=kwargs.get("genre")
        data=Movie.objects.filter(genre=genre)
        return render(request,"genre.html",{"data":data})
    

class MovieLanguage(View):
    def get(self,request,*args,**kwargs):
        lang=kwargs.get("language")
        data=Movie.objects.filter(language=lang)
        return render(request,"language.html",{"data":data})



@method_decorator(signin_required,name="dispatch")
class WatchListView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        data=Movie.objects.get(id=id)
        WatchList.objects.create(item=data,user=request.user)
        print("Added successfully")
        return redirect("watchlist_detail")
    

@method_decorator(signin_required,name="dispatch")
class WatchListDetail(View):
    def get(self,request,*args,**kwargs):
        data=WatchList.objects.filter(user=request.user)
        return render(request,"mywatchlist.html",{"data":data})
    

@method_decorator(signin_required,name="dispatch")
class WatchListDelete(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        WatchList.objects.get(id=id).delete()
        return redirect("watchlist_detail")
    


@method_decorator(signin_required,name="dispatch")
class DiaryView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        data=Movie.objects.get(id=id)
        Diary.objects.create(item=data,user=request.user)
        print("Added successfully")
        return redirect("diary_detail")
    

@method_decorator(signin_required,name="dispatch")
class DiaryDetail(View):
    def get(self,request,*args,**kwargs):
        data=Diary.objects.filter(user=request.user) #.order_by('watched')
        return render(request,"mydiary.html",{"data":data})
    

@method_decorator(signin_required,name="dispatch")
class DiaryDelete(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Diary.objects.get(id=id).delete()
        return redirect("diary_detail")



class ProfileView(View):
    def get(self,request,*args,**kwargs):
        
        return render(request,"myprofile.html")