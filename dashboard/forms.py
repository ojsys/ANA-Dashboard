from django import forms
from .models import Farmers, NewExtensionAgents

class FarmerCreationForm(forms.ModelForm):

    class Meta:
        model = Farmers
        fields = ['partner', 'firstname', 'lastname', 'gender', 'phone_no', 'own_phone', 'crops', 'crops_other', 'farm_area', 'area_unit', 'cassava', 'yam', 'maize', 'rice', 'sorghum']

class NewExtensionAgentForm(forms.ModelForm):

    class Meta:
        model = NewExtensionAgents
        fields = ['firstname', 'lastname', 'gender', 'phone_no', 'phone_no2', 'whatsapp', 'email', 'age', 'designation', 'type_org', 'org', 'country']