from rest_framework import serializers

from .models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    # we are writing this becoz we need confirm password field in our Registration request
    password2 = serializers.CharField(style={'input_type': 'password'},
                                      write_only=True)  # input_tye use for getting password in star or dotted format

    class Meta:
        model = User
        fields = ['email', 'name', 'password', 'password2', 'tc']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    # validating password and confirm password while Registration

    def validate(self, attrs):  # insted of attrs you can use data also which getting from user with request
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError("password and confirm passwowrd doesnot match")
        return attrs

    # we design a custom model so that we need to use crete method otherwise for normal model there is no need for
    # this method

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = User
        fields = ['email', 'password']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'password']


class UserChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=255, style={"input_type": 'password'}, write_only=True)
    password2 = serializers.CharField(max_length=255, style={"input_type": 'password'}, write_only=True)

    class Meta:
        fields = ['password', 'password2']

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        user = self.context.get('user')
        if password != password2:
            raise serializers.ValidationError("password and confirm password is not matching")
        user.set_password(password)
        user.save()
        return attrs
