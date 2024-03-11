from django.forms import ModelForm
from .models import Booking, Feedback


# Code added for loading form data on the Booking page
class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"

class Logger(ModelForm):
    class Meta:
        model = Feedback
        fields = "__all__"
