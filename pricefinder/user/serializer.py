from rest_framework import serializers
from .models import Account,Url
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class AccountSerializr(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['first_name', 'last_name','mobile_no','email','id','password']
        extra_kwargs = {
                'password': {'write_only': True}
        }
    def create(self,validate_data):
        validate_data['is_active'] = True
        password = validate_data.pop('password', None)
        user = Account(
        first_name=validate_data["first_name"],
        last_name=validate_data["last_name"],
        email=validate_data["email"],
        mobile_no=validate_data["mobile_no"],
        username=validate_data["email"].split('@')[0],
    )
        if password:
            user.set_password(password)
        user.save()
        return user

class UserDataSerilizer(AccountSerializr):
     class Meta:
        model = Account
        fields = ['first_name', 'last_name','mobile_no','email','id','username']

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        serializer = UserDataSerilizer(self.user).data
        print(data)
        for k, v in serializer.items():
            data[k] = v

        return data
    
class UrlSerializer(serializers.ModelSerializer):
     class Meta:
        model = Url
        fields = '__all__'


