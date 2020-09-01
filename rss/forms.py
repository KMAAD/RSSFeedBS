from django import forms




class NewFeedForm(forms.Form):

    title       = forms.CharField(label='RSS Feed Name',widget=forms.TextInput(attrs={'class': 'sidebarForm'}))
    link        = forms.URLField(label='RSS Link',  required=True, widget=forms.TextInput(attrs={'class': 'sidebarForm'}))

    userId      = forms.IntegerField(widget=forms.HiddenInput(),required=False)

