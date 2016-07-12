from django import forms

class AddSite(forms.Form):
	link = forms.URLField(initial='http://')

class Register(forms.Form):
	username = forms.CharField()
	email = forms.EmailField()
	password = forms.CharField(max_length=32, widget=forms.PasswordInput)

class Login(forms.Form):
	username = forms.CharField()
	password = forms.CharField(max_length=32, widget=forms.PasswordInput)
'''
class ChoiceForDelete(forms.Form):
	choices = forms.ModelMultipleChoiceField(
		widget  = forms.CheckboxSelectMultiple)'''