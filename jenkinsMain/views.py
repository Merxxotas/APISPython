from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view

from jenkinsMain.helpers.nameGenerator import NAMES, generateName
from jenkinsMain.helpers.nameReader import readName


# Create your views here.
@api_view(['POST', 'GET'])
def createGetNames(request):
    """
    Creates a name based on the provided data.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: A JSON response indicating the success of the name creation.
    """
    if (request.method == 'GET'):
        return JsonResponse(
            data=NAMES,
            status=status.HTTP_200_OK,
            safe=False,
        )
    elif (request.method == 'POST'):
        generateName(request.data['name'])
        return JsonResponse(
            data={"Name": "data sucesfully created"},
            status=status.HTTP_201_CREATED,
            safe=False,
        )
