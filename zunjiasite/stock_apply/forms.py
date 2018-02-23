from django import forms
 
class AddForm(forms.Form):
    stockname = forms.IntegerField()