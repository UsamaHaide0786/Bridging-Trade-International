from .models import Category
from .serializers import CategorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CategoryViewSet(APIView):
    def get(self, request, format=None):
        if 'parent_id' in request.GET:
            queryset = Category.objects.filter(parent_id=request.GET['parent_id'])
            serializer = CategorySerializer(queryset, many=True)
            return Response(serializer.data)
        queryset = Category.objects.filter(parent_id=0)
        print(queryset)
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        def getsib(data, parent_id=0):
            obj = Category.objects.create(name=data['name'], parent_id=parent_id)
            if obj:
                parent_id = obj.id
            if 'children' in data.keys():
                for item in data['children']:
                    getsib(item, parent_id)
            return True

        response=True
        serializer = CategorySerializer(data=request.data)
        if response:
            return Response({"msg":"Added Sucessfully"}, status=status.HTTP_201_CREATED)
        return Response({"msg":"Invalid dataset"}, status=status.HTTP_400_BAD_REQUEST)
class DetialView(APIView):
    def get(self,request,pk):
        obj=Category.objects.get(id=pk)
        data=Category.objects.filter(parent_id=obj.id)
        serializer = CategorySerializer(data,many=True)
        response={}
        response['name']=obj.name
        response['children']=serializer.data

        return Response(response)