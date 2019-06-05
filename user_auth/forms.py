from django import forms 
from . models import UserAccount


class UserAccountCreateForm(forms.ModelForm):    
    
    class Meta:
        model = UserAccount
        fields = ['location', 'birth_date', 'gender']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['birth_date'].widget.attrs.update({'class': 'datepicker'})