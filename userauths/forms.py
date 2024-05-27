from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Nhập tên tài khoản'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Nhập email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Nhập mật khẩu'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Nhập lại mật khẩu'}))
    class Meta:
        model = User
        fields = ("username","email")
        # lable = {
        #     'name':'name'
        # }
        