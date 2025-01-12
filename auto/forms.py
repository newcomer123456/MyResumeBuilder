from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'foto', 'email', 'phone_number', 'address', 'role', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': field.label,
            })
            # Додаємо відступи між полями
            field.widget.attrs['style'] = 'margin-bottom: 15px;'


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)


class CustomUserDetailForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'foto', 'email', 'phone_number', 'address', 'role']