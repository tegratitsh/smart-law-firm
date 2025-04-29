from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
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

class ContactForm(forms.ModelForm):
    phone = forms.CharField(
        max_length=15,
        required=False,
        validators=[RegexValidator(regex=r'^\d{8,15}$', message="Veuillez entrer un numéro de téléphone valide.")],
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Téléphone'})
    )
    
    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'phone', 'profession', 'description']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom complet'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Téléphone'}),
            'profession': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Profession'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description', 'rows': 4}),
        }
        
class MeetingForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'phone', 'profession', 'description']
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