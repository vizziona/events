from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


from .views import (
    HomeListView,
    SpeakerListView,
    ScheduleListView,
    ParticipantListView,
    SpeakerDetailsListView,
    EventListView,
    RegisterListView,
    EventDetailsListView,
)

urlpatterns = [
    path("", HomeListView.as_view(), name="home"),
    path("speaker/", SpeakerListView.as_view(), name="speaker"),
    path("speaker/<int:pk>/", SpeakerDetailsListView.as_view(), name="speaker_details"),
    path("schedule/", ScheduleListView.as_view(), name="schedule"),
    # path('schedule/<int:pk>/', ScheduleDetailsListView.as_view(), name='schedule_details'),
    path("participants/", ParticipantListView.as_view(), name="participant"),
    # path('participants/<int:pk>/', ParticipantDetailsListView.as_view(), name='participant_details'),
    path("event/", EventListView.as_view(), name="event_list"),
    path("event/<int:pk>/", EventDetailsListView.as_view(), name="event_details"),
    path("purchase/", SpeakerListView.as_view(), name="purchase"),
    path("/register", RegisterListView.as_view(), name="register"),
]
