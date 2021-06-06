from django.urls import path
from .views import UserList, UserDetail, ProductList, ProductDetail

urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('<int:pk>/', ProductDetail.as_view()),
    path('', ProductList.as_view()),
]
