from django.views.generic import CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404, redirect

from topics.models import Topic, Comment
from topics.forms import CommentForm



class CommentCreateView (LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'topic_detail.html'
    
    
    def form_valid(self, form):
        topic = get_object_or_404(Topic, pk=self.kwargs.get('pk'))
        print("Print 111", topic)
        comment = form.save(commit=False)
        comment.topic = topic
        print("Print 222", comment.topic)
        comment.author = self.request.user
        print("Print 333", comment.author, "+++++", self.request.user)
        comment.save()
        return redirect('topic_detail', pk=topic.pk)
    
    
    # def form_valid(self, form):
    #     post = get_object_or_404(Post, pk=self.kwargs.get('pk'))
    #     user = get_object_or_404(Account, pk=self.kwargs.get('pk'))
    #     form.instance(post=post, user=user)
    #     return super().form_valid(form)
    
    # def get_redirect_url(self):
    #     return reverse('post_detail', kwargs={'pk': self.object.post.pk})
    
    
    
    # def post(self, request, *args, **kwargs):
    #     print('START')
    #     post = get_object_or_404(Post, pk=kwargs.get('pk'))
    #     # user = get_object_or_404(Account, pk=kwargs.get('pk'))
    #     form = self.get_form_class()(request.POST)
    #     print("request POST ++++", request.POST, "====POST+====",post)
    #     print("PRINT 111", user)
    #     if form.is_valid():
    #         description = form.cleaned_data.get('description')
    #         image = form.cleaned_data.get('image')
    #         author = request.user
    #         # if not Post.objects.filter(description=description).exists():
    #         #     Post.objects.create(description=description, image=image, author=author)
    #     else:
    #         form = {'text' : 'Smth went wrong, post did not create'}
    #     return redirect('post_detail')
    
    
    # def get_success_url(self):
    #     return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})
    

    
