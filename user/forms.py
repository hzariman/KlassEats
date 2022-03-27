from django import forms
from django.contrib.auth import authenticate,  get_user_model
from django.contrib.auth.forms import UserCreationForm

from user.models import User
import re

""" User = get_user_model()

class UserLoginForm (forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username = username, password = password)
            if not user:
                raise forms.ValidationError('The account does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('The user is not active')
            return super(UserLoginForm, self).clean(*args,**kwargs)

class UserRegisterForm (forms.ModelForm):
    username = forms.CharField()
    email = forms.EmailField(label = 'Email Address')
    password = forms.CharField(widget = forms.PasswordInput)
    password2 = forms.CharField(widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password2',
        ]
    
    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password!= password2:
            raise forms.ValidationError('Passwords must match')
        email_qs = User.objects.filter(email = email)
        if email_qs.exists():
            raise forms.ValidationError('Email is already in use')

        return super(UserRegisterForm, self).clean(*args, **kwargs) """


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'email' ,'first_name','last_name', 'password1', 'password2')

"""     def student_check(email):
        if not re.search(r'[a][l][i][c][e][-][s][m][i][t][h].[e][d][u].[m][y]', email):
            raise forms.ValidationError('Please enter a school email address')
    
 """

class UserLoginForm(forms.ModelForm):
    password = forms.CharField(label = 'Password', widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'password')
    

    def clean(self, *args, **kwargs):
        email = self.cleaned_data['email']
        password=self.cleaned_data['password']
        if not authenticate(email = email, password = password):
            raise forms.ValidationError('Invalid Login')
