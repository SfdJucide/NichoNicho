from django import forms
from tgcore.models import CustomerMessage


class CustomerMessageeForm(forms.ModelForm):
    message = forms.Textarea()
    
    class Meta:
        model = CustomerMessage
        fields = ('user', 'message')
        widgets = {'user': forms.HiddenInput()}
        