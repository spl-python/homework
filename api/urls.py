from django.urls import path
from rest_framework_jwt import views as view
from api import views

urlpatterns = [
    path('login/',view.ObtainJSONWebToken.as_view()),
    path('users/',views.UserDetailAPIView.as_view()),
    path('user/',views.LoginAPIView.as_view())
]