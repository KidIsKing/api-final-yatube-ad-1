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

    class Meta:
        fields = ("user", "following")
        model = Follow
        read_only_fields = ("user",)
