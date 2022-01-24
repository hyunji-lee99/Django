from rest_framework import serializers
from .models import Post,Sep

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields=(
            'data',
        )
        model=Post

class SepSerializer(serializers.ModelSerializer):
    class Meta:
        fields=(
            'title','content',
        )
        model=Sep