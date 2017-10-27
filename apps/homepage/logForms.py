from django import forms

from .models import LogGame

class LogForm(forms.ModelForm):
	class Meta:
		model = LogGame
		fields = ['game_date', 'yourScore', 'opponentScore', 'opponent' ]
