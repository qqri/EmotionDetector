from django import forms
from .models import Post
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class CreatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('user', 'title' , 'subtitle' ,'content' )

        widgets = {
            'user': forms.Select(
                attrs={'class': 'form-control', 'style': 'width: 100%', 'placeholder': '이름을 입력하세요.'}
            ),
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 100%', 'placeholder': '제목을 입력하세요.'}
            ),
            'content': forms.Textarea(),
        }