from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect

from topics.models import Topic
from topics.forms import CommentForm



class CommentCreateView (LoginRequiredMixin, FormView):
    form_class = CommentForm
    
    
    def post(self, request, *args, **kwargs):
        topic = get_object_or_404(Topic, pk=kwargs.get('pk'))
        author = request.user
        form = self.get_form_class()(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get('text')
            Topic.objects.create(author=author, text=text, topic=topic)
        else:
            form = {'text' : 'Smth went wrong, comment did not create'}
        return redirect('topic_detail', pk=topic.pk)
    
    