from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from .models import User

class CustomRegisterSerializer(RegisterSerializer):
    birth_date = serializers.DateField(required=False)
    real_name = serializers.CharField(max_length=10, required=True)
    email = serializers.EmailField(max_length=50, required=True)

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['birth_date'] = self.validated_data.get('birth_date', None)
        data_dict['real_name'] = self.validated_data.get('real_name', '')
        data_dict['email'] = self.validated_data.get('email', '')
        return data_dict

    def save(self, request):
        user = super().save(request)
        user.birth_date = self.validated_data.get('birth_date', None)
        user.real_name = self.validated_data.get('real_name', '')
        user.email = self.validated_data.get('email', '')
        user.save()
        return user
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'