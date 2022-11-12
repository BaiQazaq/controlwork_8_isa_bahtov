from django.urls import path

from topics.views.topic_list_view import TopicView
from topics.views.topic_create_view import TopicCreate
from topics.views.topic_detail_view import TopicDetailView
from topics.views.comment_create_view import CommentCreateView

urlpatterns = [
    path("", TopicView.as_view(), name='index'),
    path("add/", TopicCreate.as_view(), name='topic_creation'),
    path("detail/<int:pk>", TopicDetailView.as_view(), name='topic_detail'),
    path("detail/<int:pk>/comment/add/", CommentCreateView.as_view(), name="comment_add") 
]
    