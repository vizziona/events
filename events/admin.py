from django.contrib import admin
from .models import *
from .models import (
    Event,
    Speaker,
    Schedule,
    Participant,
    SpeakerDetail,
    EventList,
    Register,
    EventDetail,
)

admin.site.register(Event)
admin.site.register(Speaker)
admin.site.register(Schedule)
admin.site.register(Participant)
admin.site.register(SpeakerDetail)
admin.site.register(EventList)
admin.site.register(Register)
admin.site.register(EventDetail)
