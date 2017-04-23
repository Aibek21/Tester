from django import forms

class ResultForm(forms.Form):
    result = forms.BooleanField(required=False)
