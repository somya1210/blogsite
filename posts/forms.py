from django import forms

from .models import Post,Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content','author','status','slug')
        widgets = { # change attribute of the original class to
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control','value':'','id':'auth','type':'hidden'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),

        }
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('name','body')
        widgets={
            #'post':forms.TextInput(attrs={'class':'form-control','value':'','id':'postsave'}),
            'name':forms.TextInput(attrs={'class':'form-control','value':'','id':'user'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
            #'date_added':forms.TextInput(attrs={'class':'form-control','value':'','id':'autodate'}),

        }
