from rest_framework import serializers
from phonebook.models import Contact, User

class ContactSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = Contact
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['id','user','username']
