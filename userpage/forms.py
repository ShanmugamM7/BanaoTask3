from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserDetails,BlogPost,Appointment

class SignupForm(UserCreationForm):
    USER_TYPE_CHOICES = (
        ('P', 'Patient'),
        ('D', 'Doctor'),
    )

    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, widget=forms.RadioSelect)
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = UserDetails
        fields = ['user_type', 'first_name', 'last_name', 'profile_picture', 'username', 'email', 'password1', 'password2',
                  'address_line1', 'city', 'state', 'pincode']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
       
        # Set help_text to an empty string for each field
        for field_name, field in self.fields.items():
            field.help_text = None
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        # Check if the passwords match
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data
    
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class BlogPostForm(forms.ModelForm):
    # Define category choices
    CATEGORY_CHOICES = (
        ('Mental Health', 'Mental Health'),
        ('Heart Disease', 'Heart Disease'),
        ('Covid19', 'Covid19'),
        ('Immunization', 'Immunization'),
    )

    # Use ModelChoiceField for category with the Category model
    category = forms.ChoiceField(choices=CATEGORY_CHOICES)

    class Meta:
        model = BlogPost
        fields = ['category', 'title', 'summary', 'content', 'image', 'draft']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5}),
        }

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['speciality', 'date_of_appointment', 'start_time_of_appointment']
        widgets = {
            'date_of_appointment': forms.DateInput(attrs={'type': 'date'}),
            'start_time_of_appointment': forms.TimeInput(attrs={'type': 'time'}),
        }