from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import AdvUser, Order


class RegisterForm(UserCreationForm):
    class Meta:
        model = AdvUser
        fields = ("username", "password1", "password2", "photo")

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for field_name in ('username', 'password1', 'password2', 'photo'):
            self.fields[field_name].help_text = ''


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"
        widgets = {'user': forms.HiddenInput, 'product': forms.HiddenInput}


class SearchForm(forms.Form):
    search_query = forms.CharField(label='Поиск', max_length=100, required=False)
