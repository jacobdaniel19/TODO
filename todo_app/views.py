from django.shortcuts import render,redirect
from django.views.generic import View
from todo_app.forms import Register,Login_form,Task_form
from todo_app.models import User,task_model
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.utils.decorators import method_decorator 

# Create your views here.

def sigin_required(fn):

    def wrapper(request,**kwargs):

        if not request.user.is_authenticated:

            return redirect("signin")
        
        else:

            return fn(request,**kwargs)
        
    return wrapper    

def mylogin(fn):

    def wrapper(request,**kwargs):

        id=kwargs.get("pk")

        obj=task_model.objects.get(id=id)

        if obj.user!=request.user:

            return redirect("signin")
        
        else:

            return fn(request,**kwargs)
        
    return wrapper    



class Registration(View):

    def get(self,request,**kwargs):

        form=Register()

        return render (request,"register.html",{"form":form})
    
    def post(self,request,**kwargs):

        form=Register(request.POST)

        if form.is_valid():

            #ORM QUERY :: to hide password we use in registration /  user login
            #create_user :: to encrupt password
            User.objects.create_user(**form.cleaned_data)
            
            #form.save()

            form=Register()

        return render (request,"register.html",{"form":form})    


class Update_user(View):

    def get(self,request,**kwargs):

        id=kwargs.get("pk")

        data=User.objects.get(id=id)

        form=Register(instance=data)

        return render (request,"register.html",{"form":form})
    
    def post(self,request,**kwargs):

        id=kwargs.get("pk")

        data=User.objects.get(id=id)

        form=Register(request.POST,instance=data)

        if form.is_valid():

            User.objects.create_user(**form.cleaned_data)

        return redirect("signin")
    
        

    
class Sign_in(View):

    def get(self,request,**kwargs):

        form= Login_form()

        return render (request,"login.html",{"form":form})  


    def post(self,request,**kwargs):

        form= Login_form(request.POST)

        if form.is_valid():

            print(form.cleaned_data)

            u_name=form.cleaned_data.get("username")  

            pwd=form.cleaned_data.get("password")

            user_obj=authenticate(username=u_name,password=pwd)

            if user_obj:

                print("Valid credientials")

                login(request,user_obj)

                return redirect("index")
            
            else:

                print("incorrect credientials")

                form=Login_form()

                return render (request,"login.html",{"form":form})
            
@method_decorator(sigin_required,name="dispatch")
class Add_task(View):

    def get (self,request,**kwargs):

        form=Task_form()

        data=task_model.objects.filter(user=request.user).order_by('completed')

        return render (request,"index.html",{"form":form,"data":data})

    def post (self,request,**kwargs):

        form=Task_form(request.POST)
                #task name ,task_description
        if form.is_valid():

            form.instance.user=request.user
                #request.user = get the authenticated user or login user

            
            form.save()

            messages.success(request,"task added successfully")

            form=Task_form()

        data=task_model.objects.all()      #read

        return render(request,"index.html",{"form":form,"data":data})  
    

@method_decorator(sigin_required,name="dispatch")
@method_decorator(mylogin,name="dispatch")
class Delete_task(View):

    def get (self,request,**kwargs):

        id=kwargs.get("pk")

        task_model.objects.get(id=id).delete()

        
        return redirect("index")
    
class Edit_task(View):

    def get(self,request,**kwargs):   

        id=kwargs.get("pk")

        obj=task_model.objects.get(id=id)

        if obj.completed == False:

            obj.completed = True
            obj.save()

        return redirect("index")  

class Sign_out(View):

    def get (self,request) :

        logout(request)

        return redirect("signin")    
    
class User_del(View):

    def get(self,request,**kwargs):

        id=kwargs.get("pk")

        User.objects.get(id=id).delete()

        return redirect("index")

