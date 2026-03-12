from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Post, Comment, Group, Follow, User


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        fields = ("id", "author", "text", "pub_date", "image", "group")
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        fields = ("id", "author", "text", "created", "post")
        model = Comment
        read_only_fields = ("author", "post")


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "title", "slug", "description")
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(slug_field="username", read_only=True)
    following = SlugRelatedField(
        slug_field="username",
        queryset=User.objects.all()
    )

    class Meta:
        fields = ("user", "following")
        model = Follow

    def validate(self, data):
        request = self.context.get("request")
        current_user = request.user
        following_user = data["following"]

        # нельзя подписаться на себя
        if current_user == following_user:
            raise serializers.ValidationError(
                "Нельзя подписаться на самого себя!")

        # проверка на дубликат подписки
        if Follow.objects.filter(
            user=current_user,
            following=following_user
        ).exists():
            raise serializers.ValidationError(
                "Вы уже подписаны на этого пользователя!")

        return data
