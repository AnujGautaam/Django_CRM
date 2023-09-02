# this is where the registration form will be designed 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 
from .models import Record
#this is how the class is created which acts like the schema and this is the method for the estimation of the signup register 
class signUpForm(UserCreationForm):
    email= forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'enter email here'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'enter first_name here'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 
    'placeholder':'enter last_name here'}))
    
    
    
    class Meta:
        model= User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


    def __init__(self, *args, **kwargs):
                super(signUpForm, self).__init__(*args, **kwargs)
                self.fields['username'].widget.attrs['class'] = 'form-control'
                self.fields['username'].widget.attrs['placeholder'] = 'User Name'
                self.fields['username'].label = ''
                self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'
                self.fields['password1'].widget.attrs['class'] = 'form-control'
                self.fields['password1'].widget.attrs['placeholder'] = 'Password'
                self.fields['password1'].label = ''
                self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'
                self.fields['password2'].widget.attrs['class'] = 'form-control'
                self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
                self.fields['password2'].label = ''
                self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	



# this form is to be an interesting one mainly because this will be created on teh basis o the model that we had created earlier 
class AddRecordForm(forms.ModelForm):
    first_name =forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'class':"form-control", 'placeholder':'2023-08-21 17:37:44'}), label='')
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'class':"form-control", 'placeholder':'last_name'}), label='')
    email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'class':"form-control", 'placeholder':'email'}),  label='')
    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'class':"form-control", 'placeholder':'phone'}), label='')
    address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'class':"form-control", 'placeholder':'address'}), label='')
    city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'class':"form-control", 'placeholder':'city'}), label='')
    state = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'class':"form-control", 'placeholder':'state'}), label='')
    zip_code = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'class':"form-control", 'placeholder':'zip  code'}), label='')

    class Meta:
          model= Record
          exclude = {'user',}