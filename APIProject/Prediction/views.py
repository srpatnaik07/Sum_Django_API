from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from  rest_framework.views import APIView


# Function based view
@api_view(['GET','POST'])
def api_add(request):
    sum = 0
    response_dict = {}
    if request.method =='GET':
        pass  ##Do nothing
    elif request.method =='POST':
        #Add the numbers
        data = request.data
        for key in data:
            sum +=data[key]
        response_dict = {"sum":sum}
    return Response(response_dict,status=status.HTTP_201_CREATED)


#Class based view
class Add_values(APIView):
    def post(self,request,format=None):
        sum = 0
        data = request.data
        for key in data:
            sum +=data[key]
        response_dict = {"sum":sum}
        return Response(response_dict,status=status.HTTP_201_CREATED)
    

