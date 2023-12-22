# serializers.py

from rest_framework import serializers
from .models import Member

class ReactSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Member
        fields = ['Topic', 'Description', 'By', 'Date', 'Image']
        extra_kwargs = {
            'Image': {'required': False}  # Make the Image field optional
        }
