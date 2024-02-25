from django import forms
from .models import Farmers

class FarmerCreationForm(forms.ModelForm):

    class Meta:
        model = Farmers
        fields = ['index', 'partner', 'firstname', 'lastname', 'gender', 'phone_no', 'own_phone', 'crops', 'crops_other', 'farm_area', 'area_unit','cassava', 'yam', 'maize', 'rice', 'sorghum']
