from django import forms
from .models import EmailMessage

class EmailMessageForm(forms.ModelForm):
    class Meta:
        model = EmailMessage
        fields = ('subject', 'message')
