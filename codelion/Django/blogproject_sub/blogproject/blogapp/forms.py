from django import forms

class BlogForm(forms.Form):
    title = forms.CharField(max_length=200)
    body = forms.CharField(widget=forms.Textarea)


from .models import Blog, Comment

class BlogModelForm(forms.ModelForm): # 애초에 form의 존재부터 model을 기반으로 만들어짐
    class Meta:
        model = Blog
        fields = '__all__' # Blog 객체 안에 있는 모든 오브젝트를 입력받는다.
        #fields = ['title', 'body']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']