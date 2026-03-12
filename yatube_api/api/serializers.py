from rest_framework import serializers
from rest_framework.relations import SlugRelatedField


from posts.models import Post, Comment, Group, Follow


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = ("id", "author", "text", "pub_date", "image", "group")
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = ("id", "author", "text", "created", "post")
        model = Comment


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "title", "slug", "description")
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("user", "following")
        model = Follow
