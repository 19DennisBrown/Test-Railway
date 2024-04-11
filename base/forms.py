from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user','description', 'location', 'surname', 'kra_pin', 'company', 'net_income', 'age', 'loan_amount', 'id_no']

    description = forms.CharField(
       label='Description',
       max_length=50,
       widget=forms.TextInput(attrs={
          'class': 'border p-1 rounded-md m-4'
       })
    )   
    surname = forms.CharField(
       label='Surname',
       max_length=50,
       widget=forms.TextInput(attrs={
          'class': 'border p-2 rounded-md m-4'
       })
    )   
    age = forms.CharField(
       label='Age must be above 18 yrs : ',
       max_length=50,
       widget=forms.TextInput(attrs={
          'class': 'border p-2 rounded-md m-4'
       })
    )   
    net_income = forms.CharField(
       label='Net Income : ',
       max_length=50,
       widget=forms.TextInput(attrs={
          'class': 'border p-2 rounded-md m-4'
       })
    )   
    company = forms.CharField(
       label='Company employed at : ',
       max_length=50,
       widget=forms.TextInput(attrs={
          'class': 'border p-2 rounded-md m-4'
       })
    )   
    loan_amount = forms.CharField(
       label='Enter amount to borrow : ',
       max_length=50,
       widget=forms.TextInput(attrs={
          'class': 'border p-2 rounded-md m-4'
       })
    )   
    id_no = forms.CharField(
       label='ID no : ',
       max_length=50,
       widget=forms.TextInput(attrs={
          'class': 'border p-2 rounded-md m-4'
       })
    )   
    kra_pin = forms.CharField(
       label='KRA Pin',
       max_length=50,
       widget=forms.TextInput(attrs={
          'class': 'border p-2 rounded-md m-4'
       })
    )   
    location = forms.CharField(
       label='location',
       widget=forms.TextInput(attrs={
          'class':'border p-2 rounded-md m-4'
       })
    ) 

class CustomForm(UserCreationForm):
  class Meta:
    model = User
    fields = UserCreationForm.Meta.fields

  username = forms.CharField(widget = forms.TextInput(attrs={
        'placeholder': 'eg Jay',
        'class': 'w-25  my-3 rounded-md border-0 py-2 pl-7 pr-20 text-gray-900 ring-1 ring-inset ring-gray-300 md:placeholder-gray-900 md:focus:placeholder-red-600 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6'
    }) ,label='Username')
  password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'password as *****',
        'class': 'w-25  my-3 rounded-md border-0 py-2 pl-7 pr-20 text-gray-900 ring-1 ring-inset ring-gray-300 md:placeholder-gray-900 md:focus:placeholder-red-600 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6'
    }), label='Password')
  password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'password again as *****',
        'class': 'w-25  my-3 rounded-md border-0 py-2 pl-7 pr-20 text-gray-900 ring-1 ring-inset ring-gray-300 md:placeholder-gray-900 md:focus:placeholder-red-600 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6'
    }), label='Password again!')

