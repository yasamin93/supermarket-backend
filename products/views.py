from django.contrib.auth import get_user_model
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
