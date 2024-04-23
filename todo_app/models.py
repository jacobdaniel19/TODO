from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class task_model(models.Model):

    task_name=models.CharField(max_length=90)

    task_description=models.TextField(null=False)

    task_created_date=models.DateField(auto_now_add=True)

    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    completed=models.BooleanField(default=False)