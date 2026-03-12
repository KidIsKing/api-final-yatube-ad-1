from django.urls import path, include
# импортируем класс роутера и вьюсеты
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, GroupViewSet, FollowViewSet, CommentViewSet

# создаём объект роутера и регистрируем вьюсеты для маршрутов
router = DefaultRouter()

router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register('follow', FollowViewSet)

router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename="comment"
)

urlpatterns = [
    # подключаем эндпоинты через роутер
    path("", include(router.urls)),
]
