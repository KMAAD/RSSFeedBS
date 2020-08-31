from django import forms

from .models import Feed


class NewFeedForm(forms.Form):

    title       = forms.CharField(label='RSS Feed Name',widget=forms.Textarea(attrs={'class': 'sidebarForm'}))
    link        = forms.URLField(label='RSS Link',  required=True)

    userId      = forms.IntegerField(widget=forms.HiddenInput(),required=False)

