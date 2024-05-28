from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers import Registration,Todoserializer
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework import status,authentication,permissions
from todo_app.models import task_model


# Create your views here.

class Userregister(APIView):

    def post(self,request,*args,**kwargs):

        serializer=Registration(data=request.data)

        if serializer.is_valid():

            serializer.save()

        return Response(serializer.data,status=status.HTTP_201_CREATED)    


class TaskViewsetview(ViewSet):


    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def list(self,request,*args,**kwargs):

        qs=task_model.objects.all()

        serializer=Todoserializer(qs,many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)

    def create(self,request,*args,**kwargs):

        serializer=Todoserializer(data=request.data)

        if serializer.is_valid():

            serializer.save(user=request.user)

        return Response (serializer.data)    
    
    def update(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=task_model.objects.get(id=id)

        serializer=Todoserializer(data=request.data,instance=qs)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)    
        
        else:

            return Response(serializer.errors,status=status.HTTP_403_FORBIDDEN)
        

    def retrieve(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=task_model.objects.get(id=id)

        serializer=Todoserializer(qs)

        return Response(serializer.data,status=status.HTTP_200_OK) 

    def destroy(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=task_model.objects.get(id=id)

        if qs.user==request.user:
            
            qs.delete()

            return Response({"message":" Todo task deleted"})

        else:

            return Response({"message":"not allowed"})
        

class TodoModelViewsetview(ModelViewSet):

    queryset=task_model.objects.all()
    serializer_class=Todoserializer
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated] 

    def get_queryset(self):
        return task_model.objects.filter(user=self.request.user)   

    def perform_create(self, serializer):
        return serializer.save()

    def perform_update(self, serializer):
        return super().perform_update(serializer)  
    

    #def perform_destroy(self, instance):
    #    instance=task_model.objects.get
    #    return 