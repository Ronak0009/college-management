from django import forms
from .models import Branch
from students.models import Student
from django.utils.safestring import mark_safe
import re

class editforms(forms.ModelForm):
    class Meta:
        model=Student
        fields= [
            'firstName',
            'middleName',
            'lastName',
            'username',
            'account_id',
            'enrolment',
            'mobile',
            'branch',
            'sem',
            'email',
            'gender',
            'isPending',
        ]


class AddBranchForm(forms.ModelForm):
    branch_name = forms.CharField(label='Department:',min_length=2, max_length=70,
                widget=forms.TextInput(attrs={"placeholder":"Enter Department Name",
                                             "size":"40",
                                             "class":"text",
                                             "name":"branchname"}))
    code = forms.CharField(label='Department Code:',max_length=2, min_length=2,
                widget=forms.TextInput(attrs={"placeholder":"Enter Department Code",
                                             "size":"40",
                                             "class":"text",
                                             "name":"branchCode"}))
    description = forms.CharField(label='Description:',max_length=500,required=False,
                widget=forms.Textarea(attrs={"placeholder":"Enter Description",
                                             "size":"40",
                                             "class":"text",
                                             "height":"5",
                                             "width":"100",
                                             "name":"description"}))

    class Meta:
        model=Branch
        fields = [
            'branch_name',
            'code',
            'description',
        ]
    
    def clean(self, *args, **kwargs):
        cleaned_data = super().clean()
        branchName = str(self.cleaned_data.get("branch_name"))
        branchCode = str(self.cleaned_data.get("code"))
        description = str(self.cleaned_data.get("description"))

        try:
            nameNotValid = False
            if not re.search("^[A-za-z\s]+$", branchName):
                branchNameError = "Not a valid name."
                nameNotValid = True
                raise forms.ValidationError(branchNameError)
        except forms.ValidationError as e:
            self.add_error('branch_name', e)
        
        if nameNotValid == False:
            try:
                if Branch.objects.filter(branch_name=branchName):
                    branchExistsError = "Department already exists."
                    branchExistsError = mark_safe(branchExistsError)
                    raise forms.ValidationError(branchExistsError)
            except forms.ValidationError as e:
                self.add_error('branch_name', e)
        try:
            codeNotValid = False
            if not re.search("^[0-9]+$", branchCode):
                branchCodeError = "Not a valid code."
                branchCodeError = mark_safe(branchCodeError)
                raise forms.ValidationError(branchCodeError)
        except forms.ValidationError as e:
            self.add_error('code', e)

        if codeNotValid == False:
            try:
                if Branch.objects.filter(code=branchCode):
                    codeExistsError = "Code already exists."
                    codeExistsError = mark_safe(codeExistsError)
                    raise forms.ValidationError(codeExistsError)
            except forms.ValidationError as e:
                self.add_error('code', e)
            else:
                return cleaned_data
        else:
            return cleaned_data

class EditBranchForm(forms.ModelForm):
    branch_name = forms.CharField(label='Department:',min_length=2, max_length=70,
                widget=forms.TextInput(attrs={"placeholder":"Enter Department Name",
                                             "size":"40",
                                             "class":"text",
                                             "name":"branchname"}))
    code = forms.CharField(label='Department Code:',max_length=2, min_length=2,
                widget=forms.TextInput(attrs={"placeholder":"Enter Department Code",
                                             "size":"40",
                                             "class":"text",
                                             "name":"branchCode"}))
    description = forms.CharField(label='Description:',max_length=500,required=False,
                widget=forms.Textarea(attrs={"placeholder":"Enter Description",
                                             "size":"40",
                                             "class":"text",
                                             "height":"5",
                                             "width":"100",
                                             "name":"description"}))

    class Meta:
        model=Branch
        fields = [
            'branch_name',
            'code',
            'description',
        ]
    
    def clean(self, *args, **kwargs):
        cleaned_data = super().clean()
        branchName = str(self.cleaned_data.get("branch_name"))
        branchCode = str(self.cleaned_data.get("code"))
        description = str(self.cleaned_data.get("description"))

        try:
            nameNotValid = False
            if not re.search("^[A-za-z\s]+$", branchName):
                branchNameError = "Not a valid name."
                nameNotValid = True
                raise forms.ValidationError(branchNameError)
        except forms.ValidationError as e:
            self.add_error('branch_name', e)
        
        if nameNotValid == False:
            try:
                if branchName != self.instance.branch_name:
                    if Branch.objects.filter(branch_name=branchName):
                        branchExistsError = "Department already exists."
                        print("hello")
                        branchExistsError = mark_safe(branchExistsError)
                        raise forms.ValidationError(branchExistsError)
            except forms.ValidationError as e:
                self.add_error('branch_name', e)
        try:
            codeNotValid = False
            if not re.search("^[0-9]+$", branchCode):
                branchCodeError = "Not a valid code."
                branchCodeError = mark_safe(branchCodeError)
                raise forms.ValidationError(branchCodeError)
        except forms.ValidationError as e:
            self.add_error('code', e)

        if codeNotValid == False:
            try:
                if branchCode != self.instance.code:
                    if Branch.objects.filter(code=branchCode):
                        codeExistsError = "Code already exists."
                        codeExistsError = mark_safe(codeExistsError)
                        raise forms.ValidationError(codeExistsError)
            except forms.ValidationError as e:
                self.add_error('code', e)
            else:
                return cleaned_data
        else:
            return cleaned_data