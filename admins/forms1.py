from django import forms
from staff.models import Staff

class editforms1(forms.ModelForm):
    class Meta:
        model=Staff
        fields= [
            'firstName',
            'middleName',
            'lastName',
            'username',
            'account_id',
            'mobile',
            'branch',
            'email',
            'gender',
            'isPending',
        ]