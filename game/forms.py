from django import forms
from django.forms import ClearableFileInput
from game.models import Game


class GameCreationForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['title','min_num_ppl', 'max_num_ppl','min_time', 'max_time',
                  'preparation', 'explanation', 'tip', 'image']

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '게임명을 입력하세요'}),
            'image': ClearableFileInput,
        }

    def __init__(self, *args, **kwargs):
        super(GameCreationForm, self).__init__(*args, **kwargs)
        self.fields['title'].required = True  # 필수 필드 설정