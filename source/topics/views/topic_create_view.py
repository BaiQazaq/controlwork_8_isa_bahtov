from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect

from topics.models import Topic
from topics.forms import TopicForm


class TopicCreate(LoginRequiredMixin, CreateView):
    template_name = 'topic_create.html'
    form_class = TopicForm
    model = Topic
    
    def post(self, request, *args, **kwargs):
        form = self.get_form_class()(request.POST, request.FILES)
        
        if form.is_valid():
            title = form.cleaned_data.get('title')
            description = form.cleaned_data.get('description')
            author = request.user
            if not Topic.objects.filter(title=title, author=author).exists():
                Topic.objects.create(description=description, title=title, author=author)
        else:
            form = {'text' : 'Smth went wrong, post did not create'}
        return redirect('index')
    
    
    def get_success_url(self):
        return reverse_lazy('index', kwargs={'pk': self.object.pk})
    