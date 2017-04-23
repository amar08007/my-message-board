""" Api Related URLS """
from api import views
from django.conf.urls import patterns, url, include

urlpatterns = [
    url(r'^msg-board/post-msg$', views.PostMessage.as_view(), name='post_message'),
    url(r'^msg-board/delete-msg$', views.DeleteMessage.as_view(), name='delete_message'),
    url(r'^msg-board/delete-all-msgs$', views.DeleteAllMessages.as_view(), name='delete_messages'),
    url(r'^msg-board/get-all-msgs$', views.GetAllMessages.as_view(), name='get_all_messages'),
]