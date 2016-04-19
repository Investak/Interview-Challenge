from django import forms
from .models import *


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(CompanyForm, self).clean()
        return cleaned_data


class ProfileForm(forms.ModelForm):
    # TODO: Define other fields here

    class Meta:
        model = Profile
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(ProfileForm, self).clean()
        return cleaned_data


class PortfolioForm(forms.ModelForm):

    class Meta:
        model = Portfolio
        fields = ['name', 'companies']

    def __init__(self, *args, **kwargs):
        super(PortfolioForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(PortfolioForm, self).clean()
        return cleaned_data

class ContactForm(forms.Form):
    name = forms.CharField(max_length=150)
    email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
