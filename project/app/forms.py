from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from django.core.validators import MaxValueValidator
from django.forms import ModelForm
from app.models import *




class UserRegisterationForm(UserCreationForm):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['username','first_name','last_name','email','password1', 'password2']


class CommitteeCreationForm(ModelForm):
    class Meta:
        model = Committee
        fields = ['committee_name','committee_members_limit',
        'committee_amount_per_month',
         'committee_starting_date']
        # widgets = {
        #             'committee_name': forms.TextInput(attrs={'class': 'form-control'}),
        #             'committee_members_limit': forms.TextInput(attrs={'class': 'form-control'}),
        #             'committee_amount_per_month': forms.TextInput(attrs={'class': 'form-control'}),
        #             'committee_starting_date': forms.TextInput(attrs={'class': 'form-control'}),      
        #         }

class CommitteeJoinForm(ModelForm):
    class Meta:
        model = Participants
        fields = [ 'participants_payment_slip']
        
       
