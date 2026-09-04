from django import forms
from .models import ChaiVarity

class ChaiVarityForm(forms.Form):
    # chai_varity = forms.ModelChoiceField
    #(query = ChaiVarity.objects.all(), label = 'select chai variety'
    chai_varity = forms.CharField()