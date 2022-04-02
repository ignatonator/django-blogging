from django import forms
from django.forms import models
from .models import Comment
class PostShare(forms.Form):
    name=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder': 'Imię'}))
    email=forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Twój Email'}))
    to=forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email odbiorcy'}))
    comment=forms.CharField(required=False, widget=forms.Textarea(attrs={'placeholder':'Twój komentarz'}))
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('name','email','body')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nazwa'}),
            'email':forms.TextInput(attrs={"placeholder":"E-mail"}),
            'body': forms.Textarea(
                attrs={'placeholder': 'Twój komentarz'}),
        }
    def clean(self):
 
       
        super(CommentForm, self).clean()
         
        email= self.cleaned_data.get('email')
        body = self.cleaned_data.get('body')
       
 
        if Comment.objects.filter(body=body,email=email).count()>0:
            self._errors['body'] = self.error_class([
                'Już udostępniłeś/aś taki komentarz'])
        
        return self.cleaned_data
class SearchForm(forms.Form):
    query=forms.CharField()

