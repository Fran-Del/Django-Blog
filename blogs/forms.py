from django import forms
from .models import Comment


class ContactForm(forms.Form):
    name = forms.CharField(label='Your Name')
    subject = forms.CharField(label='Subject')
    senders_email = forms.EmailField(label='Your Email')
    message = forms.CharField(widget=forms.Textarea, label='')

    class Meta:
        fields = ['name', 'subject', 'senders_email', 'message']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'email', 'text')
