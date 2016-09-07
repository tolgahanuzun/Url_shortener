from django import forms

class AddSite(forms.Form):
	CHOICES = (
        ('Yes_Ads', 'Yes Advertiment'),
        ('Not_Ads', 'Not Advertiment'),

    )
	link = forms.URLField(initial='http://')
	advertiment=forms.ChoiceField(choices=CHOICES, required=True, label='Example')

'''
class ChoiceForDelete(forms.Form):
	choices = forms.ModelMultipleChoiceField(
		widget  = forms.CheckboxSelectMultiple)'''