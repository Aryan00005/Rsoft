from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Role , UserRole




class SuperadminUserSerializer(serializers.ModelSerializer):
    role = serializers.CharField(write_only=True)


    class Meta:
        model = User
        fields = ('id', 'username', 'email','password' , 'role')
        extra_kwargs = {
            'password':{'write_only':True}
        }

    def create(self,validated_data):
        role_name = validated_data.pop('role')
        password = validated_data.pop('password')
        user = User.objects.create_user(password=password,**validated_data)

        role, created = Role.objects.get_or_create(name=role_name)
        UserRole.objects.create(user=user, role=role)
        return user
    
    def update(self, instance, validated_data):
        role_name = validated_data.pop('role',None)
        password = validated_data.pop('password',None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password:
            instance.set_password(password)

        instance.save()

        if role_name:
            role, created = Role.objects.get_or_create(name=role_name)
            UserRole.objects.update_or_create(user = instance,defaults={'role':role})
        
        return instance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class RegisterSerializer(serializers.ModelSerializer):
    role = serializers.CharField(write_only=True,required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password','role')

    def create(self, validated_data):
        role_name = validated_data.pop('role',None)
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password'],
        )
        if role_name:
            role, created = Role.objects.get_or_create(name=role_name) 
            UserRole.objects.create(user=user, role=role)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True , write_only=True)


