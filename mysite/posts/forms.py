from django import forms

from posts import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'price','message','category')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'price': forms.TextInput(attrs={'class': 'textinputclass'}),
            'message': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }
