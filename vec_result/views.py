from django.shortcuts import render
from rest_framework.response import Response
from .models import PinkIT
from .serializers import PinkITSerializer
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404


class PinkItTable(APIView):

    def get(self, requset):
        resultsIT = PinkIT.objects.all()
        serializer = PinkITSerializer(resultsIT, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PinkITSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateView(APIView):
    def get_object(self, pk):
        try:
            return PinkIT.objects.get(pk=pk)
        except PinkIT.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        ResultIT = self.get_object(pk)
        serializer = PinkITSerializer(ResultIT)
        return Response(serializer.data)

    def put(self, request, pk):
        resultIT = self.get_object(pk)
        serializer = PinkITSerializer(resultIT, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        resultIt = self.get_object(pk)
        resultIt.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ApiOverView(APIView):
    def get(self, request):
        api_urls = {
            'ResultsIT_Total': 'results/IT',
            'ResultIT': 'results/IT/<int:id>/',

        }
        return Response(api_urls)
