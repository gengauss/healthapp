from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from apps.healthtracker.models import Profile, Food


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class SelectFoodForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('food_selected', 'quantity',)

    def __init__(self, user, *args, **kwargs):
        super(SelectFoodForm, self).__init__(*args, **kwargs)
        self.fields['food_selected'].queryset = Food.objects.filter(person_of=user)


class AddFoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ('name', 'quantity', 'calorie')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('calorie_goal',)
