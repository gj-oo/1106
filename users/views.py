from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

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

# 获取当前用户信息视图
class MeView(APIView):
    authentication_classes = [JWTAuthentication]  # 设置JWT认证
    permission_classes = [permissions.IsAuthenticated]  # 只有已认证的用户能访问

    def get(self, request):
        user = request.user  # 从请求中获取当前用户
        return Response(UserSerializer(user).data)
