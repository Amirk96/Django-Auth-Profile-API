from rest_framework.serializers import ModelSerializer
from myprofile.models import MyProfileModel

class MyProfileSerializer(ModelSerializer):
    class Meta:
        model = MyProfileModel
        fields = ['id', 'first_name', 'last_name', 'mobile', 'email', 'user']