from django import forms
class ProfileForms(forms.Form):
    user_image=forms.FileField()