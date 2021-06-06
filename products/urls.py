from .views import UserViewSet, ProductViewSet
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', ProductViewSet, basename='products')
urlpatterns = router.urls
