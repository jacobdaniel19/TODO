from django import forms
from todo_app.models import User,task_model


#for registration


class Register(forms.ModelForm):
    class Meta:

        model=User
        fields=['username','first_name',"last_name","email","password"]

class Task_form(forms.ModelForm):
    class Meta:

        model=task_model  
        fields=["task_name","task_description"]  
        widgets={
            'task_name':forms.TextInput(attrs={'class':'forms-control','placeholder':"enter the task name"}),
            'task_description':forms.Textarea(attrs={'class':'form-control','column':20,'row':5,'placeholder':"enter the task description"})
        }


#for sign_in 


class Login_form(forms.Form):

    username=forms.CharField()
    password=forms.CharField()