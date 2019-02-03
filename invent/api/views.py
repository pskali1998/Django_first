from django.shortcuts import render
#MAIN CODE OF API
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Items

class ItemsView(APIView):
    def get(self,request): #get request will return test and val as pass
        if 'name' in request.GET:
            #name variable present in GET
            data = Items.objects.filter(name=request.GET['name']).values('name','price').first()
        else:
            data = Items.objects.all().values('name','price')
        return Response({"result":data},status=200)
    def post(self,request):
        data = request.data
        print(data)
        Item_obj = Items.objects.create(name=data['name'], price=data['price'])
        return Response({"message":"created"}, status=202)