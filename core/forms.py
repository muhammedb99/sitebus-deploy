from django import forms
from .models import Photo

class LoginForm(forms.Form):
    username = forms.CharField(label="שם משתמש")
    password = forms.CharField(widget=forms.PasswordInput, label="סיסמה")

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ["image", "caption"]
        labels = {"image": "בחר תמונה", "caption": "כותרת (לא חובה)"}
