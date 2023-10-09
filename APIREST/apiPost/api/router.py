from rest_framework.routers import DefaultRouter
from apiPost.api.views import registerApiViewSet,loginApiViewSet

router_posts = DefaultRouter()

router_posts.register(prefix='register', basename='register', viewset=registerApiViewSet)
router_posts.register(prefix='login', basename='login', viewset=loginApiViewSet)