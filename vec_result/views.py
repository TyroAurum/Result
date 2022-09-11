from telnetlib import STATUS
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import PinkIT
from .serializers import PinkITSerializer
from rest_framework import status

# Create your views here.


@api_view(['GET'])
def apiOverView(request):
    api_urls = {
        'ResultsIT_Total': 'results/IT',
        'ResultIT': 'result/IT/<int:id>'

    }
    return Response(api_urls)


@api_view(['GET'])
def getResultsIT(request):
    resultsIT = PinkIT.objects.all()
    serializer = PinkITSerializer(resultsIT, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getResultIT(request, pk):
    resultIT = PinkIT.objects.get(id=pk)
    serializer = PinkITSerializer(resultIT, many=False)
    return Response(serializer.data)
