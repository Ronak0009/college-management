from django import forms
# from .models import AppUser
from django.utils.safestring import mark_safe
import re

class LoginForm(forms.Form):
    username = forms.CharField(label='Username:', min_length=6, max_length=40,
                widget=forms.TextInput(attrs={"placeholder":"Your Username",
                                             "size":"40",
                                             "class":"text",
                                             "name":"username"}))
    
    passwd = forms.CharField(label='Password:', min_length=8, max_length=40,
                widget=forms.PasswordInput(attrs={"placeholder":"Your Password",
                                             "size":"40",
                                             "class":"text",
                                             "name":"password"}))
    # class Meta:
    #     model = AppUser
    #     fields = [
    #         'username',
    #         'passwd'
    #     ]

    def clean(self, *args, **kwargs):
        cleaned_data = super().clean()
        username = str(self.cleaned_data.get("username"))
        passwd = str(self.cleaned_data.get("passwd"))

        try:
            username_not_valid = False
            if not re.search(r'^\w+$', username):
                username_error = mark_safe("Invalid username")
                username_not_valid = True
                raise forms.ValidationError(username_error)
        except forms.ValidationError as e:
            self.add_error('username', e)

        try:
            if not re.search(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$',passwd):
                errormsg = mark_safe('Invalid password')
                raise forms.ValidationError(errormsg)
        except forms.ValidationError as e:
            self.add_error('passwd', e)

        else:
            return cleaned_data

