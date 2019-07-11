from django import forms
from polls.models import users

class EntryForm(forms.ModelForm):
	class Meta:
		model = users
		fields = '__all__'
