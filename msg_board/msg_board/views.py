# Message Boards Views.py file
from backend.api_controller import ApiController
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from board.models import Message


# Main Landing Page OR '/'
@csrf_exempt
def home(request):
    """ 
        Show the home page where a user can post a message and can also access all previous 
        messages posted by other users
    """
    # Return Dict
    data = {}

    if request.method == 'POST':
        api_controller = ApiController(request)
        data_dict = api_controller.post_message()
        data.update(data_dict)
    
    # Return All Messages
    data['msgs'] = Message.objects.all().order_by('-created_at')

    return render(request, 'index.html', data)

def delete_msg(request):
    """ 
        Delete Individual Message
    """
    # Return Dict
    data = {}

    if request.method == 'GET':
        api_controller = ApiController(request)
        data_dict = api_controller.delete_message()
        data.update(data_dict)
    
    return HttpResponseRedirect('/')

def delete_all_msgs(request):
    """ 
        Delete Individual Message
    """
    # Return Dict
    data = {}

    if request.method == 'GET':
        api_controller = ApiController(request)
        data_dict = api_controller.delete_all_messages()
        data.update(data_dict)
    
    return HttpResponseRedirect('/')