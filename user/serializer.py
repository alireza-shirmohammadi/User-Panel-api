from rest_framework import serializers
from .models import Image,Manage
from drf_extra_fields.fields import Base64ImageField
from django.contrib.auth.models import User

class ImageSerializer(serializers.ModelSerializer):
    image=Base64ImageField()
    user=serializers.CharField()
    url=None
    class Meta:
        model=Image
        fields='__all__'
    def create(self,validated_data):
        image=validated_data.pop('image')
        user=validated_data.pop('user')
        user_id=User.objects.get(username=user)
        image=Image.objects.create(image=image,user=user_id)
        self.url=image.image.url
        return image
    
