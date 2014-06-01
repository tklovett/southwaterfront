from django.forms import ModelForm
from models import Resident

class ResidentForm(ModelForm):
	class Meta:
		model = Resident
		fields = ['first_name', 'last_name', 'email', 'monthly_spending']