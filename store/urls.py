from django.urls import path
from django.urls.conf import include
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet)


# URLConf
urlpatterns = router.urls
