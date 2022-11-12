from django import forms

from topics.models import Topic, Comment



class TopicForm(forms.ModelForm):

    class Meta:
        model = Topic
        fields = ('title', 'description')

    

class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Найти')
    
    
class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ['text']
        help_texts = {
                    'text' : ('Please keep mutual respect')
            }