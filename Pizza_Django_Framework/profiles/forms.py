from django import forms

from Pizza_Django_Framework.profiles.models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['email', 'password']

class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['email', 'password']

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

class DeleteProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields= '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
            field.widget.attrs['disabled'] = 'disabled'