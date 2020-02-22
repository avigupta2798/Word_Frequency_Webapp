# frequencycount/forms.py

from django import forms
from frequencycount.models import WordCountUrl

class WordCountUrlForm(forms.ModelForm):
    url = forms.CharField(widget=forms.URLInput)
    class Meta:
        model = WordCountUrl
        fields = "__all__"