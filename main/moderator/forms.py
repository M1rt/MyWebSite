from user.models import Word
from django.forms import ModelForm, TextInput, NumberInput

class WordForm(ModelForm):
    class Meta:
        model = Word
        fields = ['Slovo', 'Perevod', 'languages']
        widgets = {
            "Slovo":TextInput(attrs={
                'class':'form-control'
            }),
            "Perevod": TextInput(attrs={
                'class': 'form-control'
            }),
            "languages": TextInput(attrs={
                'class': 'form-control'
            })
        }





