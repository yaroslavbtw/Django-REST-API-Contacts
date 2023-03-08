from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from contacts.models import Contact


class ContactSerializer(ModelSerializer):

    class Meta:
        model = Contact
        exclude = ['owner']
