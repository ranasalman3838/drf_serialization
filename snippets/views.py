from rest_framework import status
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from django.http import Http404
from snippets.serializers import SnippetSerializer

from rest_framework import mixins,generics

# Create your views here.
# @api_view(['GET','POST'])
# def snippet_list(request, format=None):

#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         # data = JSONParser().parse(request)
#         serializer = SnippetSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET','PUT','DELETE'])
# def snippet_detail(request, pk, format=None):
    #retrieve, update or delete 

    # try:
    #     snippet = Snippet.objects.get(pk=pk)
    # except Snippet.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)
    
    # if request.method == "GET":
    #     serializer = SnippetSerializer(snippet)
    #     return Response(serializer.data)
    
    # elif request.method == 'PUT':
    #     # data = JSONParser().parse(request)
    #     serializer = SnippetSerializer(snippet, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    # elif request.method == 'DELETE':
    #     snippet.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)



# class SnippetList(APIView):
#     def get(self, request, format=None):
#         snippets  = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)
    
#     def post(self, request, format=None):
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class SnippetDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Snippet.objects.all()
#         except Snippet.objects.get(pk=pk):
#             raise Http404
    
#     def get(self,request,pk,fromat=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet,many=True)# if you are sending requst.data than don't use many=True and if you are sending queryset you must pass many=true
#         return Response(serializer.data)
    
#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



# class SnippetList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer

#     def get(self, request, *args, **kwargs):
#         return  self.list(request, *args, **kwargs)
    
#     def post(self,request, *args, **kwargs):
#         print(request)
#         return self.create(request, *args, **kwargs)

# class SnippetDetail(mixins.RetrieveModelMixin,
#                     mixins.DestroyModelMixin,
#                     mixins.UpdateModelMixin,
#                     generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
    
#     def get(self, request, *args, **kwargs):
#         print(request.data)
#         return self.retrieve(request, *args, **kwargs)
    
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
    
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
