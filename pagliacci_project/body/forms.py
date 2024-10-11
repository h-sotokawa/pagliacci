from django import forms
from .models import BodyComposition

class BodyCompositionForm(forms.ModelForm):
    class Meta:
        model = BodyComposition
        fields = ['weight', 'body_fat_percentage', 'muscle_mass', 'measurement_date']
        widgets = {
            'measurement_date': forms.DateInput(attrs={'type': 'date'}),
        }
