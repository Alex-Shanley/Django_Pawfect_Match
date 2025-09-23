from django import forms
from .models import Pet


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['img', 'name', 'age', 'breed', 'species']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter pet name'
            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter age',
                'min': '0',
                'max': '50'
            }),
            'breed': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter breed'
            }),
            'species': forms.Select(attrs={
                'class': 'form-control'
            }),
            'img': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['img'].required = False
