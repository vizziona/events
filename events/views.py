from django.views.generic import ListView
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


class HomeListView(ListView):
    model = Event
    template_name = "home.html"


class RegisterListView(ListView):
    model = Register
    template_name = "register.html"


class SpeakerListView(ListView):
    model = Speaker
    template_name = "speaker.html"


class ScheduleListView(ListView):
    model = Schedule
    template_name = "schedule.html"


class ParticipantListView(ListView):
    model = Participant
    template_name = "participants.html"


class EventListView(ListView):
    model = EventList
    template_name = "event.html"


class SpeakerDetailsListView(ListView):
    model = SpeakerDetail
    template_name = "speaker_details.html"


class EventDetailsListView(ListView):
    model = EventDetail
    template_name = "event_details.html"
