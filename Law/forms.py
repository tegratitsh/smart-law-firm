from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Contact, Folder , Meeting, Area


class LoginForm(forms.Form):

    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom complet'}),
        label="Nom complet"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mot de passe'}),
        label="Mot de passe"
    )

class ContactForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom complet'}),
        label="Nom complet"
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        label="Email"
    )
    phone = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Téléphone'}),
        label="Téléphone"
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Votre message', 'rows': 5}),
        label="Message"
    )
    


class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['full_name', 'email', 'phone', 'profession', 'topic','description',]
        
class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ['full_name', 'email', 'phone', 'date', 'heure', 'topic', 'message']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'heure': forms.TimeInput(attrs={'type': 'time'}),
        }



class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['name', 'topic', 'image', 'tag', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'}),
            'topic': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sujet'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tag'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description', 'rows': 5}),
        }