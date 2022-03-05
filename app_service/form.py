from django.forms import ModelForm

from app_service.models import Appointment


class CustomerForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['phone_number'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['time'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['time_zone'].widget.attrs = {
            'class': 'form-control col-md-6'
        }

    class Meta:
        model = Appointment
        fields = ['name', 'phone_number', 'time', 'time_zone']
