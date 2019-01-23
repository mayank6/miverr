from django.forms import ModelForm
from .models import Gig
from django import forms

class GigForm(ModelForm):
    status = forms.BooleanField(help_text="Tick to active the post or blank to bookmark",required=False)
    class Meta:
        model=Gig
        fields=["title","category","description","price","photo","status",]
