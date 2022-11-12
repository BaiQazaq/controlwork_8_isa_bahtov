from django.views.generic import DetailView

from topics.models import Topic
from topics.forms import CommentForm


class TopicDetailView(DetailView):
    template_name = 'topic_detail.html'
    model =  Topic
    pk_url_kwarg = 'pk'
    context_object_name = 'topic'
    
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TopicDetailView, self).get_context_data(object_list=object_list, **kwargs)
        context['comment_form'] = CommentForm()
        post = self.object
        comments = post.comments.order_by('author')
        context['comments'] = comments
        return context
    
    