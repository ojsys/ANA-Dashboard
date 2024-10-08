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
import json
from django.core.serializers.json import DjangoJSONEncoder



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
    active_farmers = EventParticipants.objects.aggregate(
        total_farmers=Sum('no_participants')
    )
    events = Events.objects.all()
    events_count = Events.objects.count()
    event_participants = EventParticipants.objects.all()
    
    # Get all Extension Agents
    extension_agents = ExtensionAgents.objects.all()
    
    # Maximum number of EAS

    ea_count = extension_agents.count()
    top_eas = extension_agents.values('org').annotate(total_eas=Count('org')).order_by('-total_eas').distinct()[:10]
    partner_farmers = Dissemination.objects.values('partner').annotate(
        total_farmers = Sum('farmers_M') + Sum('farmers_F')
    ).order_by('-total_farmers')[:10] # Sorting by the total farmers reached

    # Find the maximum number of farmers reached by any single partner
    max_farmers = partner_farmers[0]['total_farmers'] if partner_farmers else 0

    # Calculate the percentage for each partner
    for partner in partner_farmers:
        partner['percentage'] = (partner['total_farmers'] / max_farmers) * 100 if max_farmers > 0 else 0

    
    date = datetime.date.today()

    total_farmers = farmers.count()
    male_farmers = farmers.filter(gender='male').distinct().count()
    female_farmers = farmers.filter(gender='female').distinct().count()
    # Aggregate farmers by location
    farmers_data = Dissemination.objects.filter(country='Nigeria').exclude(city='NA').values('city').annotate(
        male_farmers=Sum('farmers_M'),
        female_farmers=Sum('farmers_F'),
        total_farmers=Sum('farmers_M') + Sum('farmers_F')
    ).order_by('-total_farmers')[:10]

    locatons_city = [data['city'] for data in farmers_data]
    male_farmers_city = [data['male_farmers'] for data in farmers_data]
    female_farmers_city = [data['female_farmers'] for data in farmers_data]

    # Prepare data for the chart (serialize it into JSON format)
    data = json.dumps(list(farmers_data), cls=DjangoJSONEncoder)

    temperature = get_weather(location)

    context = {
        'user': user,
        'partner': partner,
        'location': location,
        'country': country,
        'data': data, 
        'partners': partners, 
        'male_farmers': male_farmers,
        'female_farmers': female_farmers,
        'active_farmers': active_farmers, 
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
        'partner_farmers': partner_farmers,
        'temperature': temperature,
        'locations_city': locatons_city,
        'male_farmers_city': male_farmers_city,
        'female_farmers_city': female_farmers_city,
        'farmers_data': data,
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