from django.urls import path

from movies.views import MoviesAPIView, CommentsAPIView

urlpatterns = [
    path(r'movies/', MoviesAPIView.as_view(), name='movies'),
    path(r'comments/', CommentsAPIView.as_view(), name='comments'),
]
