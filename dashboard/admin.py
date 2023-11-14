from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Dissemination, Partner, Events, EventParticipants, ExtensionAgents, Farmers




admin.site.register(Dissemination)
admin.site.register(Partner)
admin.site.register(Events)
admin.site.register(EventParticipants)
admin.site.register(ExtensionAgents)
admin.site.register(Farmers)