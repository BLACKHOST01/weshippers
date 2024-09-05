"""
Forms for the API.
"""

from django import forms
from .models import  Shipment
from django.contrib.auth.forms import (
    AuthenticationForm, PasswordResetForm, SetPasswordForm,
)



class CustomSignInForm(AuthenticationForm):
    """
    Form for custom sign-in.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['autofocus'] = True
        self.fields['password'].widget.attrs['autocomplete'] = 'current-password'
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
        self.fields['username'].widget.attrs['required'] = True


class CustomSignOutForm(forms.Form):
    """
    Form for custom sign-out.
    """

    reason = forms.CharField(required=False)





class ShipmentForm(forms.ModelForm):
    """
    Form for creating and editing shipments.
    """

    class Meta:
        model = Shipment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['from_country'].widget.attrs['autofocus'] = True


class SetPasswordForm(SetPasswordForm):
    """
    Form for setting a new password.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_password1'].widget.attrs['autofocus'] = True
        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['placeholder'] = 'Enter your new password'
        self.fields['new_password1'].widget.attrs['required'] = True
        self.fields['new_password1'].widget.attrs['maxlength'] = 254
        self.fields['new_password1'].widget.attrs['type'] = 'password'
        self.fields['new_password1'].widget.attrs['id'] = 'id_new_password1'
        self.fields['new_password1'].widget.attrs['name'] = 'new_password1'
        self.fields['new_password1'].widget.attrs['autocomplete'] = 'new-password'
        self.fields['new_password1'].widget.attrs['placeholder'] = 'New Password'

        self.fields['new_password2'].widget.attrs['autofocus'] = True
        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm your new password'
        self.fields['new_password2'].widget.attrs['required'] = True
        self.fields['new_password2'].widget.attrs['maxlength'] = 254
        self.fields['new_password2'].widget.attrs['type'] = 'password'
        self.fields['new_password2'].widget.attrs['id'] = 'id_new_password2'
        self.fields['new_password2'].widget.attrs['name'] = 'new_password2'
        self.fields['new_password2'].widget.attrs['autocomplete'] = 'new-password'
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm Password'

