from ckeditor.widgets import CKEditorWidget
from django import forms, views
from .models import Blog


class BlogForm(forms.ModelForm):
    title = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Title', 'class': 'form-control', 'unicorn:model': 'title'}))
    image = forms.FileField(required=False)
    description = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control'}))
    # more can be read here https://www.webforefront.com/django/modelformrelationships.html

    
    

    class Meta:
        model = Blog
        fields = ['title','image', 'description']