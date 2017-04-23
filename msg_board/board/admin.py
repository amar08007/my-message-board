from django.contrib import admin
from django.contrib.admin import ModelAdmin
from board.models import Message, SecretToken

# Register your models here.
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'msg_text', 'msg_source', 'sender_name', 'created_at')

# Register your models here.
class SecretTokendmin(admin.ModelAdmin):
    list_display = ('token', 'created_at')

admin.site.register(SecretToken, SecretTokendmin)
admin.site.register(Message, MessageAdmin)
