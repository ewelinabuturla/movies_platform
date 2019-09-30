from rest_framework import serializers

from movies.models import Movies, Comments

class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'

    def create(self, validated_data):
        return Movies.objects.create(**validated_data)

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'

    def create(self, validated_data):
        return Comments.objects.create(**validated_data)
