from django import forms

class NameForm(forms.Form):
	username = forms.CharField(max_length = 255, widget = forms.TextInput(attrs = {'class': 'type-message',
		                                                                           'name': 'type-message'}))