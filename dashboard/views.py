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
    partners2_count = Partner.objects.values_list('partner', flat=True).distinct().count()

    male_farmers = Dissemination.objects.aggregate(total=Sum('farmers_M'))
    female_farmers = Dissemination.objects.aggregate(total=Sum('farmers_F'))
    
    return render(request, 'dashboard/index.html', 
                  {'data': data, 'partners': partners, 'male_farmers': male_farmers,
                    'female_farmers': female_farmers, 'partners_count': partners_count, 'partners2_count': partners2_count})
    

@login_required
def dashboard_view(request):
    data = Dissemination.objects.all()
    partners = Dissemination.objects.aggregate(total=Count('partner'))

    partners_count = Dissemination.objects.values_list('partner', flat=True).distinct().count()

    male_farmers = Dissemination.objects.aggregate(total=Sum('farmers_M'))
    female_farmers = Dissemination.objects.aggregate(total=Sum('farmers_F'))
    
    return render(request, 'dashboard/dashboard.html', 
                  {'data': data, 'partners': partners, 'male_farmers': male_farmers,
                    'female_farmers': female_farmers, 'partners_count': partners_count})



