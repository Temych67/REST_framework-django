from rest_framework import serializers
from chat.models import Chat
from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField
    )


class ChatSenderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Chat
		fields = ('email','message')


class MessageDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Chat
		fields = ('email','message','date_published','date_updated')