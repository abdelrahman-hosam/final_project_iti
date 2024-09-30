from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
class CustomAuthenticationForm(AuthenticationForm):
    def _init_(self, *args, **kwargs):
        super(CustomAuthenticationForm, self)._init_(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'custom-class', 'placeholder': 'Username'})
        self.fields['password'].widget.attrs.update({'class': 'custom-class', 'placeholder':'Password'})

class user_signup(forms.ModelForm):
    username = forms.CharField(max_length= 200 , required=True , label='username' , widget=forms.TextInput)
    password = forms.CharField(max_length=150 , required=True , label='password' , widget= forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username' , 'password']
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('username is already taken')
        else:
            return username
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError('password must be more than 8 characters')
        else:
            return password
    def save_user(self , commit = True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user