from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='home'),
    path('menu-items/', views.MenuList.as_view()),
    path('menu-items/<int:pk>', views.MenuDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('api-token-auth/', obtain_auth_token),
]