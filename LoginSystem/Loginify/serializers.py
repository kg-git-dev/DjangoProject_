from rest_framework import serializers
from .models import UserDetails
from django.contrib.auth.hashers import make_password

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ['Username', 'Email', 'Password']