from rest_framework import serializers
from users.models import NewUser

class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ('email', 'user_name', 'password') # 필수 입력 필드
        extra_kwargs = {'password': {'write_only': True}} # 비밀번호가 옳다는 추가 인수 정의(보안) 

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance 
        