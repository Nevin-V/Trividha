from django.contrib import admin
from form.models import main_events
from form.models import events
from form.models import school
from form.models import participant_details
# Register your models here.
admin.site.register(main_events)
admin.site.register(events)
admin.site.register(school)
admin.site.register(participant_details)