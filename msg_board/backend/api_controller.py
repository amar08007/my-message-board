# backend/controller/edutap_controller.py
"""
    This script will be used to do all backend tasks for edutap api

"""

from datetime import datetime
from django.db import connection
from django.forms.models import model_to_dict
from board.models import Message, SecretToken
import traceback
# import global_variables as Globals

class ApiController(object):
    """ 
        Class containing functions related to routing all views for
        message board api
    """

    def __init__(self, request):
        """ Initialize a user with all the details """
        self.request = request


    # Get IP Address for Client from Request, taken from Stackoverflow
    def get_client_ip(self):
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[-1].strip()
        else:
            ip = self.request.META.get('REMOTE_ADDR')
        return ip

    def is_valid_token(self, token):
        """ Check if given secret token is valid or not """
        try:
            if SecretToken.objects.filter(token=token).exists():
                return True
            else:
                return False
        except:
            return False

    def post_message(self):
        """ Post Message sent by the user """
        # Post Params
        # Return Dict
        data = {}

        try:
            # Validate Inputs
            if 'text' not in self.request.POST.keys():
                data['message'] = 'Message could not be posted, there is no text to be posted'
                data['success'] = False
                return data

            msg_text = str(self.request.POST.get('text'))
            msg_source = self.get_client_ip()
            email = str(self.request.POST.get('email'))
            name = str(self.request.POST.get('name'))

            # Preprocess Data
            name = 'anonymous' if name in ['None', ''] else name

            new_msg = Message(msg_text=msg_text, \
                              msg_source=msg_source, \
                              sender_name=name, \
                              sender_email=email)
            new_msg.save()
            data['message'] = 'Message posted successfully'
            data['success'] = True
            data['message_id'] = new_msg.id
        except:
            print traceback.print_exc()
            data['message'] = 'Message could not be posted, please try again'
            data['success'] = False
        return data

    def get_all_messages(self):
        """ Get All Message """
        # Return Dict
        data = {}
        data['msgs'] = []
        data['count'] = 0

        # Check if order provided
        order = self.request.GET.get('order')

        try:
            if order == 'asc':
                all_msgs = Message.objects.all().order_by('created_at')
            else:
                all_msgs = Message.objects.all().order_by('-created_at')
            for msg in all_msgs:
                tmp_dict = model_to_dict(msg)
                tmp_dict['created_at'] = str(msg.created_at)
                data['msgs'].append(tmp_dict)
                data['count'] += 1
            data['success'] = True
        except:
            print traceback.print_exc()
            data['success'] = False
            data['message'] = 'Messages could not pulled'

        return data

    def delete_message(self):
        """ Delete Message """
        # Return Dict
        data = {}

        msg_id = self.request.GET.get('id')
        token = str(self.request.GET.get('token'))

        try:
            if self.is_valid_token(token):
                Message.objects.get(pk=msg_id).delete()
                data['success'] = True
                data['message'] = 'Message deleted successfully'
            else:
                data['success'] = False
                data['message'] = 'Invalid Token, Message could not be deleted'
        except:
            print traceback.print_exc()
            data['success'] = False
            data['message'] = 'Message ID not found, Message could not be deleted'

        return data

    def delete_all_messages(self):
        """ Delete All Messages """
        # Return Dict
        data = {}
        token = str(self.request.GET.get('token'))
        print token
        try:
            if self.is_valid_token(token):
                Message.objects.all().delete()
                data['success'] = True
                data['message'] = 'Messages deleted successfully'
            else:
                data['success'] = False
                data['message'] = 'Invalid Token, Messages could not be deleted'
        except:
            print traceback.print_exc()
            data['success'] = False
            data['message'] = 'Messages could not be deleted, please try again later'

        return data


       