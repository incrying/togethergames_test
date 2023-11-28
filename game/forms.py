from django import forms
from django.forms import ClearableFileInput
from game.models import Game


class GameCreationForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['title','min_num_ppl', 'max_num_ppl','min_time', 'max_time',
                  'preparation', 'explanation', 'tip', 'image']

        widgets = {
            'image': ClearableFileInput,
        }