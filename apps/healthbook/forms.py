from django import forms

from apps.healthbook.models import Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '例：鈴木太郎'}), label=False)
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': '例：abc123@gmail.com'}), label=False)
    feedback = forms.TextField(widget=forms.Textarea(attrs={'placeholder': '言いたいことはここに'}), label=False)

    class Meta:
        model = Contact
        fields = ['name', 'email', 'feedback']
