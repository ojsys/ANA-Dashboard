from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Count, Sum
from django.views import View
from .models import Dissemination, EventParticipants, Events, ExtensionAgents, Partner, Farmers



@login_required
def index(request):
    data = Dissemination.objects.all()
    partners = Partner.objects.all()[:10]

    partners_count = Dissemination.objects.values_list('partner', flat=True).distinct().count()
    partners2_count = Partner.objects.values_list('partner', flat=True)

    farmers = Farmers.objects.all()

    male_farmers = farmers.filter(gender='male').distinct().count()
    female_farmers = farmers.filter(gender='female').distinct().count()



    
    return render(request, 'dashboard/index.html', 
                  {'data': data, 'partners': partners, 'male_farmers': male_farmers,
                    'female_farmers': female_farmers, 'partners_count': partners_count, 'partners2_count': partners2_count})
    

