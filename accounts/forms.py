from django import forms
from .models import Account, UserProfile

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Enter Password'
    }))
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Enter Password'
    }))
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'email', 'address', 'password' ]

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Last Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email'
        self.fields['address'].widget.attrs['placeholder'] = 'Enter Address'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password != password_confirm:
            raise forms.ValidationError(
                'Password does not match.'
            )
            
class UserForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'email')
        
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Last Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

        
class UserProfileForm(forms.ModelForm):
    profile_picture = forms.ImageField(required=False, error_messages = {'invalid':("images files only")}, widget=forms.FileInput)
    class Meta:
        model = UserProfile
        fields = ('address_1', 'address_2', 'city', 'state', 'country', 'profile_picture')
        
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['address_1'].widget.attrs['placeholder'] = 'Address 1'
        self.fields['address_2'].widget.attrs['placeholder'] = 'Address 2'
        self.fields['city'].widget.attrs['placeholder'] = 'City'
        self.fields['state'].widget.attrs['placeholder'] = 'State'
        self.fields['country'].widget.attrs['placeholder'] = 'Country'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        