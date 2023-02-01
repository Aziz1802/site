from apps.user.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Введите имя', 'class':'login-input' }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Введите фамилию', 'class':'login-input' }))
    username= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Имя пользователя', 'class':'login-input' }))
    email= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Введите электронную почту','class':'login-input', 'type':'email'}))
    password1= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Введите пароль', 'class':'login-input', 'type':'password'}))
    password2= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Потвердите пароль', 'class':'login-input', 'type':'password'}))
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

class UserLoginForm(AuthenticationForm):
    username= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Имя пользователя', 'class':'login-input' }))
    password= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Введите пароль', 'class':'login-input', 'type':'password'}))
    class Meta:
        model = User
        fields = ('username', 'password')

class UserProfileform(UserChangeForm):
    first_name= forms.CharField(widget=forms.TextInput(attrs={'class':'form.control','placeholder':'Введите имя'}))
    last_name= forms.CharField(widget=forms.TextInput(attrs={'class':'form.control','placeholder':'Введите Фамилию'}))
    image=forms.CharField(widget=forms.TextInput(attrs={'class':'form.control'}))
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form.control','placeholder':'Введите имя пользователя','readonly':True}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form.control','placeholder':'Введите email','readonly':True}))
class Meta:
    model=User
    fields=('first_name','last_name','image','username','email')