from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm
from models import Resident

class ResidentForm(ModelForm):
	class Meta:
		model = Resident
		fields = ['first_name', 'last_name', 'email', 'weekly_spending']
		labels = {
            'weekly_spending': _('Estimated weekly grocery spending'),
        }