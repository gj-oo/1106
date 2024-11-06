from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
import jwt
from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed
from .models import User

# 注册视图
class SignupView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 登录视图
class SigninView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MeView(APIView):
    # 禁用默认认证机制
    authentication_classes = []  # 这样会绕过默认的 JWT 认证
    
    def get(self, request):
        # 从 Authorization header 中提取 token
        auth_header = request.headers.get('Authorization')

        if not auth_header:
            raise AuthenticationFailed('Authorization header missing.')

        # 获取 token 部分，去掉 "Bearer " 前缀
        token = auth_header.split(' ')[1]

        # 获取数据库中的用户信息
        user = User.objects.filter(id=1).first()

        # 返回id和email
        return Response({'id': user.id, 'email': user.email}, status=200)
