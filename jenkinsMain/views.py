from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

from jenkinsMain.helpers import name_manager
from jenkinsMain.helpers.nameReader import read_names


# Create your views here.
@api_view(['POST', 'GET'])
def create_get_names(request):
    """
    Creates a name based on the provided data.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: A JSON response indicating the success of the name creation.
    """
    if request.method == 'GET':
        return JsonResponse(
            data=read_names(),
            status=status.HTTP_200_OK,
            safe=False
        )
    elif request.method == 'POST':
        name_manager.generate_name(request.data['name'])
        return JsonResponse(
            data={"message": "data successfully created"},
            status=status.HTTP_201_CREATED,
            safe=False
        )


@api_view(['PUT'])
def update_name(request, name_id: int):
    """
    Updates the name with the provided ID.

    Args:
        request (HttpRequest): The HTTP request object.
        name_id (int): The ID of the name to update.

    Returns:
        JsonResponse: A JSON response indicating the success of the name update.
    """
    name_manager.update_name(name_id, request.data['name'])
    return JsonResponse(
        data={"message": "data successfully updated"},
        status=status.HTTP_200_OK,
        safe=False
    )
