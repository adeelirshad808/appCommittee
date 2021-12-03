from django.contrib import admin
from .models import *


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', ]
   

class CommitteeAdmin(admin.ModelAdmin):
    list_display = ['committee_creator', 'committee_name',
                    'committee_members_limit', 'committee_amount_limit',
                    'committee_month_period',
                     'committee_starting_date', 'committee_ending_date']
   
   

class ParticipantsAdmin(admin.ModelAdmin):
    list_display = ['participants_name',  'participants_committee_name',
                    'participants_paid_status', 'participants_amount_paid', 'participants_payment_slip']
   



admin.site.register(Profile,ProfileAdmin)
admin.site.register(Committee,CommitteeAdmin)
admin.site.register(Participants,ParticipantsAdmin)