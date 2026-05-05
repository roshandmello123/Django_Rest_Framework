from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status


@api_view(['GET','POST','PUT','DELETE'])
def student_api(request,pk=None):

    print("req===>",request)
    if request.method=="GET": 
        id=pk
        if id is not None:
            stu=Student.objects.get(id=id) 
            print("stu--->",stu)
            serilizer=StudentSerializer(stu)
            print("serializer--->",serilizer)
            print("serializer.data--->",serilizer.data)
            return Response(serilizer.data)

        stu=Student.objects.all()
        print("stu of all==>",stu)
        serilizer=StudentSerializer(stu,many=True)
        print("serializer inside many===>",serilizer)
        return Response(serilizer.data)

    if request.method=="POST":
        serializer=StudentSerializer(data=request.data)
        print("serializer inside post--->",serializer)
        if serializer.is_valid():
            print("serialzier inside if-->",serializer)
            serializer.save()
            return Response({'mgs':'data created'},status=status.HTTP_201_CREATED)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)

    
    if request.method=='PUT':
        id=pk
        print("id inside put--->",id)
        stu=Student.objects.get(pk=id)
        print("stu inisde put===>",stu)
        serializer=StudentSerializer(stu,data=request.data)
        print("serilazer iniside put-->",serializer)
        if serializer.is_valid():
            print("serialzier iniside if --->",serializer)
            serializer.save()
            return Response({'mgs':'Data Updated'})
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)


    if request.method=='DELETE':
        stu=Student.object.get( id=pk)
        stu.delete()
        return Response({'mgs':'Data Deleted'})
    


 