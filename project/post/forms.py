from django import forms


class AddPost(forms.Form):
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea())