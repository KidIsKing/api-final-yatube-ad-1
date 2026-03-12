from django.shortcuts import get_object_or_404

from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

from posts.models import Post, Group, Follow, Comment
from .serializers import (
    PostSerializer,
    GroupSerializer,
    FollowSerializer,
    CommentSerializer
)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        """Автоматически заполняем поле автора именем пользователя."""
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied(
                "У вас недостаточно прав для выполнения данного действия.")
        super().perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied(
                "У вас недостаточно прав для выполнения данного действия.")
        super().perform_destroy(instance)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    # просмотр подписок неавторизованным пользователям запрещён
    permission_classes = (IsAuthenticated,)
    search_fields = ("following__username",)

    def perform_create(self, serializer):
        """Автоматически заполняем поле юзера именем пользователя."""
        serializer.save(user=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        return Comment.objects.filter(post_id=post_id)

    # def perform_create(self, serializer):
    #     serializer.save(
    #         author=self.request.user,
    #         post_id=self.kwargs.get("post_id")
    #     )

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied(
                "У вас недостаточно прав для выполнения данного действия.")
        super().perform_destroy(instance)
