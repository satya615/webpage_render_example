from django import forms
from .models import *
from django.core.validators import EmailValidator 
class log_in(forms.ModelForm):
    class Meta:
        model=Login
        fields='__all__'
        widgets = {
            'password': forms.PasswordInput(), 
        }
    username = forms.CharField(validators=[EmailValidator()])


class admin_menu(forms.ModelForm):
    class Meta:
        model=Menu
        fields=["num","items","price","item_type","image"]
        widgets={
            "num":forms.TextInput(attrs={
                'type':'hidden',
                "readonly":True,
            })
        }
