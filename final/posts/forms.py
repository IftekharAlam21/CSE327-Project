from django import forms

from posts.models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'price','message','category')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'price': forms.TextInput(attrs={'class': 'textinputclass'}),
            'message': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }
    def form_valid(self, form):
        postform=form.save(commit=False)
        postform.post=self.kwargs.get(pk)
        postform.save()
        super().form_valid(form)
