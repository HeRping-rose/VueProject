from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    """简化的用户序列化器：只做数据转换，不包含验证逻辑"""
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'phone', 'nickname', 'avatar')
        extra_kwargs = {'password': {'write_only': True}}  # 密码仅写入


class LoginSerializer(serializers.Serializer):
    """登录序列化器：只定义输入字段"""
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)