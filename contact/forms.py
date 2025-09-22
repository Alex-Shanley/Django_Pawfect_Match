from django import forms
from .models import Submission


class ContactForm(forms.ModelForm):
    """Form for contact submissions"""
    class Meta:
        model = Submission
        fields = ['first_name', 'surname', 'email', 'message', 'terms']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your first name'
            }),
            'surname': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your surname'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your message',
                'rows': 5
            }),
            'terms': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['terms'].required = True
        self.fields['terms'].label = 'I agree to the terms and conditions'