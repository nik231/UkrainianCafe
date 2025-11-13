from django import forms
from .models import StaffMember

class StaffMemberForm(forms.ModelForm):
    class Meta:
        model = StaffMember
        fields = ['first_name', 'last_name', 'position', 'hire_date', 'phone_number', 'email', 'is_active', 'hourly_wage']
        widgets = {
            'hire_date': forms.DateInput(attrs={'type': 'date'}),
        }
