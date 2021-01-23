from django import forms
from datetime import datetime
from common.models import Announcement

class announcementform(forms.Form):
    title=forms.CharField(label='Title:', min_length=6, max_length=40,
                widget=forms.TextInput(attrs={"placeholder":"Title",
                                             "size":"40",
                                             "class":"text",
                                             "name":"title"}))
    description=forms.CharField(label='Decription:', min_length=6, max_length=40,
                widget=forms.TextInput(attrs={"placeholder":"Description",
                                             "size":"40",
                                             "class":"text",
                                             "name":"description"}))
class Meta:
    model=Announcement
    fields=[
        'title',
        'description',
    ]
    