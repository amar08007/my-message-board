""" 
    msg_board URL Configuration
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    # Standard URLS
    url(r'^$', 'msg_board.views.home', name='home'),
    url(r'^delete-msg$', 'msg_board.views.delete_msg', name='delete_msg'),
    url(r'^delete-all-msgs$', 'msg_board.views.delete_all_msgs', name='delete_all_msgs'),

    # Rest API URLS
    url(r'^api/', include('api.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
