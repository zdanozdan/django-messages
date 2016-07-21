from django.core.paginator import Paginator
from rest_framework import serializers,pagination
from django_messages.models import Message

class MessagesSerializer(serializers.ModelSerializer):
    sender = serializers.CharField(source='sender.username', read_only=True)
    recipient = serializers.CharField(source='recipient.username', read_only=True)    
    class Meta:
        model = Message
        #exclude = ('id','user')
