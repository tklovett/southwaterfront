from django.forms import ModelForm
from models import Resident

class ResidentForm(ModelForm):
	class Meta:
		model = Resident
		fields = ['given_name', 'family_name', 'email']