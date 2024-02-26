from django.db import models


class Dissemination(models.Model):
    today = models.DateTimeField(auto_now_add=True)
    firstNameEN = models.CharField(max_length=255, blank=True)
    surNameEN = models.CharField(max_length=255, blank=True)
    phoneNrEN = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    orgEN = models.CharField(max_length=255, blank=True)
    partner = models.CharField(max_length=255, blank=True)
    event = models.CharField(max_length=255, blank=True)
    title = models.TextField(blank=True)
    startdate = models.DateField()
    participant_list = models.BooleanField(default=False)
    farmers_M = models.IntegerField(default=0)
    farmers_F = models.IntegerField(default=0)


    def __str__(self):
        return self.event + self.title + self.startdate + self.orgEN + self.partner




class Partner(models.Model):
    index = models.IntegerField(default=None)
    country = models.CharField(max_length=100, blank=True)
    partner = models.CharField(max_length=100, blank=True)
    partnerfull = models.CharField(max_length=100, blank=True)
    sector = models.CharField(max_length=100, blank=True)
    partner_type = models.CharField(max_length=100, blank=True)
    vc_segmain = models.CharField(max_length=100, blank=True)
    vc_segs = models.CharField(max_length=100, blank=True)
    integrated = models.BooleanField(default=True, null=True)
    mel_data = models.BooleanField(default=False, null=True)
    input_supply = models.BooleanField(default=False, null=True)
    production = models.BooleanField(default=False, null=True)
    digital_services = models.BooleanField(default=False, null=True)
    marketing_processing = models.BooleanField(default=False, null=True)
    financial_services = models.BooleanField(default=False, null=True)
    research = models.BooleanField(default=False, null=True)
    policy_regulation = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.partner 



class ExtensionAgents(models.Model):
    index = models.IntegerField(default=0)
    firstname = models.CharField(max_length=100, null=True)
    lastname = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=100, null=True)
    phone_no = models.CharField(max_length=100, null=True)
    phone_no2 = models.CharField(max_length=100, null=True)
    whatsapp = models.BooleanField(default=False, null=True)
    whatsapp2 = models.BooleanField(default=False, null=True)
    email = models.CharField(max_length=100, null=True)
    age = models.IntegerField(null=True)
    education = models.CharField(max_length=100, null=True)
    designation = models.CharField(max_length=100, null=True)
    type_org = models.CharField(max_length=100, null=True)
    org = models.CharField(max_length=100, null=True)
    org_other = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    area_level = models.IntegerField(null=True)
    hasc1 = models.CharField(max_length=120, null=True)
    hasc2 = models.CharField(max_length=120, null=True)
    no_farmers = models.CharField(max_length=100, null=True)
    date_added = models.DateField()
    certified = models.BooleanField(default=False, null=True)
    use_case = models.CharField(max_length=100, null=True)
    format = models.CharField(max_length=100, null=True)
    tools = models.CharField(max_length=100, null=True)
    otherakilimoexpertise = models.CharField(max_length=100, null=True)
    crops = models.CharField(max_length=100, null=True)
    crops_other = models.CharField(max_length=100, null=True)
    technologies = models.CharField(max_length=100, null=True)
    technologies_other = models.CharField(max_length=100, null=True)
    equipment = models.CharField(max_length=100, null=True)
    equipment_other = models.CharField(max_length=100, null=True)
    services = models.CharField(max_length=100, null=True)
    input_type = models.CharField(max_length=100, null=True)
    credit_types = models.CharField(max_length=100, null=True)
    market_type = models.CharField(max_length=100, null=True)
    paper = models.BooleanField(default=False, null=True)
    app = models.BooleanField(default=False, null=True)
    viamo = models.BooleanField(default=False, null=True)
    arifu = models.BooleanField(default=False, null=True)
    dashboard = models.BooleanField(default=False, null=True)
    worksheet = models.BooleanField(default=False, null=True)
    instructions = models.BooleanField(default=False, null=True)
    farmerfriendly_videos = models.BooleanField(default=False, null=True)
    short_videos = models.BooleanField(default=False, null=True)
    cartoon_guides = models.BooleanField(default=False, null=True)
    postcards = models.BooleanField(default=False, null=True)
    rya_app = models.BooleanField(default=False, null=True)
    fr = models.BooleanField(default=False, null=True)
    ic = models.BooleanField(default=False, null=True)
    wm_pp = models.BooleanField(default=False, null=True)
    sp_hs = models.BooleanField(default=False, null=True)
    input = models.BooleanField(default=False, null=True)
    credit = models.BooleanField(default=False, null=True)
    market = models.BooleanField(default=False, null=True)
    fertilizer_supply = models.BooleanField(default=False, null=True)
    herbicide_supply = models.BooleanField(default=False, null=True)
    cuttings_supply = models.BooleanField(default=False, null=True)
    mechanization = models.BooleanField(default=False, null=True)
    indirect_financial = models.BooleanField(default=False, null=True)
    individual_credit = models.BooleanField(default=False, null=True)
    group_lending = models.BooleanField(default=False, null=True)
    intermediary_credit = models.BooleanField(default=False, null=True)
    market_information = models.BooleanField(default=False, null=True)
    market_access = models.BooleanField(default=False, null=True)
    crop_insurance = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.firstname + ' ' + self.lastname + ' ' + self.org


class Events(models.Model):
    index = models.IntegerField(default=0)
    firstname = models.CharField(max_length=100, blank=True, null=True)
    lastname = models.CharField(max_length=100, null=True, blank=True)
    designation = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=100, null=True, blank=True)
    phone_no = models.CharField(max_length=20, null=True, blank=True)
    org = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    event = models.CharField(max_length=100, null=True, blank=True)
    partner = models.CharField(max_length=100, null=True, blank=True)
    partner_original = models.CharField(max_length=100, null=True, blank=True)
    hasc1 = models.CharField(max_length=120, null=True)
    hasc2 = models.CharField(max_length=120, null=True)
    city = models.CharField(max_length=100, null=True)
    venue = models.CharField(max_length=100, null=True)
    lat = models.CharField(max_length=100, null=True)
    lon = models.CharField(max_length=100, null=True)
    date_added = models.DateField(null=True, blank=True)
    startdate = models.DateField(null=True, blank=True)
    enddate = models.DateField(null=True, blank=True)
    usecase = models.CharField(max_length=50, null=True, blank=True)
    format = models.CharField(max_length=50, null=True, blank=True)
    titlefull = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    topics = models.CharField(max_length=255, null=True, blank=True)
    services = models.CharField(max_length=100, null=True)
    input_type = models.CharField(max_length=100, null=True, blank=True)
    input_orgs = models.CharField(max_length=100, null=True, blank=True)
    credit_types = models.CharField(max_length=100, null=True, blank=True)
    credit_orgs = models.CharField(max_length=100, null=True, blank=True)
    market_type = models.CharField(max_length=100, null=True, blank=True)
    market_orgs = models.CharField(max_length=100, null=True)
    paper = models.CharField(max_length=100, null=True)
    app = models.BooleanField(default=False, null=True)
    viamo = models.BooleanField(default=False, null=True)
    arifu = models.BooleanField(default=False, null=True)
    fr = models.BooleanField(default=False, null=True)
    ic = models.BooleanField(default=False, null=True)
    wm_pp = models.BooleanField(default=False, null=True)
    sp_hs = models.BooleanField(default=False, null=True)
    input = models.BooleanField(default=False, null=True)
    credit = models.BooleanField(default=False, null=True)
    market = models.BooleanField(default=False, null=True)
    fertilizer_supply = models.BooleanField(default=False, null=True)
    herbicide_supply = models.BooleanField(default=False, null=True)
    cuttings_supply = models.BooleanField(default=False, null=True)
    mechanization = models.BooleanField(default=False, null=True)
    indirect_financial = models.BooleanField(default=False, null=True)
    individual_credit = models.BooleanField(default=False, null=True)
    group_lending = models.BooleanField(default=False, null=True)
    intermediary_credit = models.BooleanField(default=False, null=True)
    market_information = models.BooleanField(default=False, null=True)
    market_access = models.BooleanField(default=False, null=True)
    crop_insurance = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.firstname + ' ' + self.lastname + ' ' + self.partner + ' ' + self.title + ' ' + self.venue





class EventParticipants(models.Model):
    index = models.IntegerField(default=0)
    partner = models.CharField(max_length=100, blank=True, null=True)
    participant = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=100, blank=True, null=True)
    no_participants = models.IntegerField()

    def __str__(self):
        return self.partner + ' ' + self.participant + ' ' + self.no_participants


CHOICES_HAS_PHONE = ((True, 'Yes'), (False, 'No'))

class Farmers(models.Model):
    index = models.IntegerField(default=0)
    partner = models.CharField(max_length=100, blank=True, null=True)
    firstname = models.CharField(max_length=100, blank=True, null=True)
    lastname = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=100, blank=True, null=True)
    phone_no = models.CharField(max_length=100, blank=True, null=True)
    own_phone = models.BooleanField(default=False, null=True, choices=CHOICES_HAS_PHONE)
    crops = models.CharField(max_length=50, null=True, blank=True)
    crops_other = models.CharField(max_length=50, null=True)
    farm_area = models.DecimalField(decimal_places=2, max_digits=2, null=True)
    area_unit = models.CharField(max_length=50, null=True, blank=True)
    cassava = models.BooleanField(default=False, null=True)
    yam = models.BooleanField(default=False, null=True)
    maize = models.BooleanField(default=False, null=True)
    rice = models.BooleanField(default=False, null=True)
    sorghum = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.firstname + ' ' + self.lastname + ' ' + self.crops + ' ' + self.farm_area + ' ' + self.area_unit
    

class NewExtensionAgents(models.Model):

    firstname = models.CharField(max_length=100, null=True)
    lastname = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=100, null=True, choices=(('Male','Male'),('Female','Female')))
    phone_no = models.CharField(max_length=100, null=True)
    phone_no2 = models.CharField(max_length=100, null=True)
    whatsapp = models.BooleanField(default=False, null=True)
    email = models.CharField(max_length=100, null=True)
    age = models.IntegerField(null=True)
    education = models.CharField(max_length=100, null=True, choices=(('Secondary','Secondary'),('Diploma','Diploma'),('Degree','Degree'),('Masters','Masters'),('PhD','PhD')))
    designation = models.CharField(max_length=100, null=True)
    type_org = models.CharField(max_length=100, null=True, choices=(('NGO','NGO'),('Government','Government'),('Private','Private')))
    org = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.firstname + ' ' + self.lastname + ' ' + self.gender + ' ' + self.phone_no + ' ' + self.email + ' ' + self.org