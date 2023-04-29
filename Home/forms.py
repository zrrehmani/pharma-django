from django import forms

class ProductForm(forms.Form):
	pid = forms.IntegerField(widget=forms.TextInput(attrs={'type':'hidden'}))
	name = forms.CharField(label='Your Name',min_length=2, required=True, widget=forms.TextInput(attrs={'class':'form-control', 'name':'name'}))
	email = forms.EmailField(label='Email', min_length=2, required=True, widget=forms.TextInput(attrs={'class':'form-control', 'name':'email'}))
	password = forms.CharField(label='Password', min_length=2, required=True, widget=forms.TextInput(attrs={'class':'form-control', 'name':'password'}))

	# def __init__(self, *args, **kwargs):
	# 	self.__init__(*args, **kwargs)
	# 	self.fields['name'].label = 'Your Name'
