"""
    Views for the api
"""
from backend.api_controller import ApiController
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView


class PostMessage(APIView):

    def post(self, request, *args, **kw):
        # Process the form data and save the message sent in the post request
        api_controller = ApiController(request)
        data_dict = api_controller.post_message()
        response = Response(data_dict, status=status.HTTP_200_OK)
        return response

class GetAllMessages(APIView):

    def get(self, request, *args, **kw):
        # Process the form data and save the message sent in the post request
        api_controller = ApiController(request)
        data_dict = api_controller.get_all_messages()
        response = Response(data_dict, status=status.HTTP_200_OK)
        return response

class DeleteMessage(APIView):

    def get(self, request, *args, **kw):
        # Process the form data and delete the message if token is valid
        api_controller = ApiController(request)
        data_dict = api_controller.delete_message()
        response = Response(data_dict, status=status.HTTP_200_OK)
        return response

class DeleteAllMessages(APIView):

    def get(self, request, *args, **kw):
        # Process the form data and delete the message if token is valid
        api_controller = ApiController(request)
        data_dict = api_controller.delete_all_messages()
        response = Response(data_dict, status=status.HTTP_200_OK)
        return response
