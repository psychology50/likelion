from django.contrib.auth import authenticate
from rest_framework import serializers
from users.models import NewUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

class RegisterUserSerializer(serializers.ModelSerializer):
    # password2 = serializers.CharField()
    class Meta:
        model = NewUser
        fields = ['email', 'user_name', 'password'] # 필수 입력 필드
        extra_kwargs = {'password': {'write_only': True}} # 비밀번호가 옳다는 추가 인수 정의(보안) 

    # def __init__(self, *args, **kwargs):
    #     # Don't pass the 'fields' arg up to the superclass
    #     fields = kwargs.pop('fields', None)

    #     # Instantiate the superclass normally
    #     super(RegisterUserSerializer, self).__init__(*args, **kwargs)

    #     if fields:
    #         # Drop any fields that are not specified in the `fields` argument.
    #         allowed = set(fields)
    #         existing = set(self.fields.keys())
    #         for field_name in existing - allowed:
    #             self.fields.pop(field_name)

    # @property
    # def data(self):
    #     d = super(RegisterUserSerializer, self).data

    #     if 'password' in d:
    #         del d['password']

    #     return d

    # def restore_object(self, attrs, instance=None):
    #     user = super(RegisterUserSerializer, self).restore_object(attrs, instance)
    #     if instance is None:
    #         user.set_password(attrs['password'])
    #     return user

    # def to_native(self, obj):
    #     if 'password2' in self.fields:
    #         self.fields.pop('password2')
    #     return super(RegisterUserSerializer, self).to_native(obj)

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance 

    def validate(self, attrs): # 중복 체크
        email = attrs['email']
        if NewUser.objects.filter(email=email).exists():
            raise serializers.ValidationError("user already exists")
        return attrs

    # def validate_password2(self, attrs, source):
    #     password2 = attrs.pop(source)
    #     if attrs['password'] != password2:
    #         raise serializers.ValidationError('password mismatch')
    #     return attrs

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = "__all__"
    

class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    class Meta:
        model = NewUser
        fields = ('old_password', 'new_password')
        extra_kwargs = {'new_password': {'write_only': True, 'required': True},
                        'old_password': {'write_only': True, 'required': True}}

    def validate_new_password(self, value):
        validate_password(value)
        return value


# class ObtainUserTokenSerializer(TokenObtainPairSerializer):

#     @classmethod
#     def get_token(cls, user):
#         token = super(ObtainUserTokenSerializer, cls).get_token(user)

#         # Add custom claims
#         token['email'] = user.email
#         return token

class RefreshTokenSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_messages = {
        'bad_token': 'Token is invalid or expired'
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token')