from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Count, Sum
from django.views import View
from .models import Dissemination, EventParticipants, Events, ExtensionAgents, NewExtensionAgents, Partner, Farmers
from .forms import FarmerCreationForm, NewExtensionAgentForm
from django.core.paginator import Paginator
import datetime
import requests



def get_weather(location):
    api_key = '7677795504e405409686392fc93047fc'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['main']['temp']  # Temperature in Celsius
    else:
        return None  # Handle error cases here

@login_required
def index(request):
    user = request.user
    partner = Partner.objects.get(partner=user.organization)
    location = user.location
    country = partner.country

    data = Dissemination.objects.all()
    partners = Partner.objects.all()
    total_partners = Partner.objects.count()

    partners_count = Dissemination.objects.values_list('partner', flat=True).distinct().count()
    partners2_count = Partner.objects.values_list('partner', flat=True)

    farmers = Farmers.objects.all()
    events = Events.objects.all()
    events_count = Events.objects.count()
    event_participants = EventParticipants.objects.all()
    
    # Get all Extension Agents
    extension_agents = ExtensionAgents.objects.all()
    
    # Maximum number of EAS

    ea_count = extension_agents.count()
    top_eas = extension_agents.values('org').annotate(total_eas=Count('org')).order_by('-total_eas').distinct()[:10]
    date = datetime.date.today()

    total_farmers = farmers.count()
    male_farmers = farmers.filter(gender='male').distinct().count()
    female_farmers = farmers.filter(gender='female').distinct().count()

    locations = [
        {'location': 'Lagos', 'country': 'Nigeria'},
        {'location': 'Enugu', 'country': 'Nigeria'},
        {'location': 'Abuja', 'country': 'Nigeria'},
    ]
    
    # For each location, fetch the temperature
    for loc in locations:
        loc['temperature'] = get_weather(loc['location'])

    context = {
        'user': user,
        'partner': partner,
        'location': location,
        'country': country,
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
        'top_eas': top_eas,
        'locations': locations,
        

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

# Displaying the EAs
@login_required
def eas(request):
    user = request.user
    partner = Partner.objects.get(partner=user.organization)
    display_org = user.organization.replace("_", " ")
    
    paginate = Paginator(NewExtensionAgents.objects.filter(org=partner).order_by('id'), 20)
    page = request.GET.get('page')
    eas = paginate.get_page(page)
    
    context = {'eas': eas, 'display_org': display_org}

    return render(request, 'dashboard/eas.html', context)

# Adding New Extension Agent
@login_required
def add_eas(request):
    form = NewExtensionAgentForm()

    context = {'form': form }
    return render(request, 'dashboard/add_eas.html', context)