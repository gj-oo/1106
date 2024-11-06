from django.urls import path
from .views import SignupView, SigninView, MeView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('signin/', SigninView.as_view(), name='signin'),
    path('me/', MeView.as_view(), name='me'),
]
