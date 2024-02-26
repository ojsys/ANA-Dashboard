from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Count, Sum
from django.views import View
from .models import Dissemination, EventParticipants, Events, ExtensionAgents, Partner, Farmers
from .forms import FarmerCreationForm
from django.core.paginator import Paginator
import datetime



@login_required
def index(request):
    data = Dissemination.objects.all()
    partners = Partner.objects.all()[:10]
    total_partners = Partner.objects.count()

    partners_count = Dissemination.objects.values_list('partner', flat=True).distinct().count()
    partners2_count = Partner.objects.values_list('partner', flat=True)

    farmers = Farmers.objects.all()
    events = Events.objects.all()
    events_count = Events.objects.count()
    event_participants = EventParticipants.objects.all()
    extension_agents = ExtensionAgents.objects.all()
    ea_count = extension_agents.count()
    date = datetime.date.today()

    total_farmers = farmers.count()
    male_farmers = farmers.filter(gender='male').distinct().count()
    female_farmers = farmers.filter(gender='female').distinct().count()



    context = {
        'data': data, 
        'partners': partners, 
        'male_farmers': male_farmers,
        'female_farmers': female_farmers, 
        'partners_count': partners_count, 
        'partners2_count': partners2_count,
        'total_partners': total_partners,
        'events': events,
        'events_count': events_count,
        'event_participants': event_participants,
        'extension_agents': extension_agents,
        'date': date,
        'farmers': total_farmers,
        'ea_count': ea_count,

    }

    
    return render(request, 'dashboard/index.html', 
                  context)
    

@login_required
def farmers(request):
    user = request.user
    partner = Partner.objects.get(partner=user.organization)
    farmers = Farmers.objects.filter(partner=partner)[:50]
    display_org = user.organization.replace("_", " ")

    # set up pagination
    paginate = Paginator(Farmers.objects.all().filter(partner=partner).order_by('id'), 20)
    page = request.GET.get('page')
    our_farmers = paginate.get_page(page)

    context = {'farmers': our_farmers, 'display_org': display_org}
    return render(request, 'dashboard/our_farmers.html', context)


@login_required
def add_farmer(request):
    form = FarmerCreationForm()

    context = {'form': form }
    return render(request, 'dashboard/add_farmer.html', context)


@login_required
def our_eas(request):
    user = request.user
    partner = Partner.objects.get(partner=user.organization)
    display_org = user.organization.replace("_", " ")
    
    paginate = Paginator(ExtensionAgents.objects.filter(org=partner).order_by('id'), 20)
    page = request.GET.get('page')
    our_eas = paginate.get_page(page)
    
    context = {'our_eas': our_eas, 'display_org': display_org}

    return render(request, 'dashboard/our_eas.html', context)