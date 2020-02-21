# frequencycount/forms.py

from django import forms
from frequencycount.models import WordCountUrl

class WordCountUrlForm(forms.ModelForm):
    class meta():
        model =WordCountUrl
        fields = ('url')