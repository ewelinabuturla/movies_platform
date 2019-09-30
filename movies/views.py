import json
import requests

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from movies.models import (
    Movies,
    Comments
)

from movies.serializer import (
    MoviesSerializer,
    CommentsSerializer
)

class MoviesAPIView(APIView):
    """
    API endpoints to manipulate Movies
    """
    http_method_name = ['get', 'post', ]

    def get(self, request, format=None):
        """
        GET list of movies
        """
        movies = Movies.objects.all()
        serializer = MoviesSerializer(movies, many=True)
        return Response({'movies': serializer.data })

    def get_by_title(self, title):
        try:
            return Movies.objects.get(title=title)
        except Movies.DoesNotExist:
            return False

    def fetch_movie_data(self, title):
        apikey = ''
        url = f'http://www.omdbapi.com/?apikey={apikey}&t={title}'
        try:
            response = requests.get(url)
        except requests.exceptions.RequestException as e:
            return
        return json.loads(response.text.lower())

    def post(self, request, format=None):
        """
        POST movie title
        """
        serializer = MoviesSerializer(data=request.data)
        if (serializer.is_valid(raise_exception=True)):
            movie_title = request.data.get('title')
            movie = self.get_by_title(movie_title)
            if (movie):
                return Response({ "movie": movie })
            else:
                movie = self.fetch_movie_data(movie_title)
                serializer = MoviesSerializer(data=movie)
                if (movie.get('title')):
                    if (serializer.is_valid(raise_exception=True)):
                        serializer.save()
                    else:
                        return Response('Not valid request, ' \
                                        'at least title is needed')
                else:
                    return Response('Movie title is not valid ' \
                                   'The title was not found in the database')

class CommentsAPIView(APIView):
    """
    API endpoints to manipulate Comments
    """
    http_method_name = ['get', 'post', ]

    def get(self, request, format=None):
        """
        GET list of comments
        """
        if (request.data.get('movie')):
            comments = Comments.objects.filter(movie=request.data.get('movie'))
            serializer = CommentsSerializer(comments, many=True)
            return Response({"Comments": serializer.data})
        else:
            comments = Comments.objects.all()
            serializer = CommentsSerializer(comments, many=True)
            return Response({"comments": serializer.data })

    def post(self, request, format=None):
        """
        POST comment for a movie
        """
        serializer = CommentsSerializer(data=request.data)
        if (serializer.is_valid(raise_exception=True)):
            serializer.save()
        else:
            return Response('Not valid request')
