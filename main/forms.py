from django import forms
from .models import Talaba, Guruh

class TalabaForm(forms.ModelForm):
    class Meta:
        model = Talaba
        fields = ['ism', 'familiya', 'email', 'telefon', 'guruh', 'tug_sanasi', 'jins', 'manzil']
        widgets = {
            'ism': forms.TextInput(attrs={'class': 'form-input', 'placeholder': "Ismni kiriting"}),
            'familiya': forms.TextInput(attrs={'class': 'form-input', 'placeholder': "Familiyani kiriting"}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': "email@example.com"}),
            'telefon': forms.TextInput(attrs={'class': 'form-input', 'placeholder': "+998 90 123 45 67"}),
            'guruh': forms.Select(attrs={'class': 'form-input'}),
            'tug_sanasi': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'jins': forms.Select(attrs={'class': 'form-input'}),
            'manzil': forms.Textarea(attrs={'class': 'form-input', 'rows': 3, 'placeholder': "Manzilni kiriting"}),
        }
        labels = {
            'ism': 'Ism', 'familiya': 'Familiya', 'email': 'Email',
            'telefon': 'Telefon', 'guruh': 'Guruh',
            'tug_sanasi': "Tug'ilgan sana", 'jins': 'Jins', 'manzil': 'Manzil',
        }

class GuruhForm(forms.ModelForm):
    class Meta:
        model = Guruh
        fields = ['nomi', 'tavsif', 'rasm']
        widgets = {
            'nomi': forms.TextInput(attrs={'class': 'form-input', 'placeholder': "Guruh nomini kiriting"}),
            'tavsif': forms.Textarea(attrs={'class': 'form-input', 'rows': 3, 'placeholder': "Guruh haqida qisqa ma'lumot"}),
            'rasm': forms.FileInput(attrs={'class': 'form-input'}),
        }
        labels = {'nomi': 'Guruh nomi', 'tavsif': 'Tavsif'}
