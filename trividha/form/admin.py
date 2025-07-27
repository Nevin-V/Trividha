from django.contrib import admin
from form.models import main_events
from form.models import events
from form.models import school
# Register your models here.
admin.site.register(main_events)
admin.site.register(events)
admin.site.register(school)