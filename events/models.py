from django.db import models


class EventList(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField()
    category = models.CharField(
        max_length=50,
        choices=(
            ("MUSIC", "Music"),
            ("SPORTS", "Sports"),
            ("SCIENCE", "Science"),
            ("TECHNOLOGY", "Technology"),
        ),
        default="FREE",
    )
    payment = models.CharField(
        max_length=4, choices=(("FREE", "Free"), ("PAID", "Paid")), default="FREE"
    )
    detail = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=200)
    category = models.CharField(
        max_length=50,
        choices=(
            ("MUSIC", "Music"),
            ("SPORTS", "Sports"),
            ("SCIENCE", "Science"),
            ("TECHNOLOGY", "Technology"),
        ),
        default="FREE",
    )
    event_access = models.CharField(
        max_length=4, choices=(("FREE", "Free"), ("PAID", "Paid")), default="FREE"
    )

    def __str__(self):
        return self.title


class Speaker(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()
    photo = models.ImageField(upload_to="images/")
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    linkedin_link = models.URLField()
    twitter_link = models.URLField()

    def __str__(self):
        return self.name


class EventDetail(models.Model):
    name = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    attended = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    shifts = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Schedule(models.Model):
    category_title = models.CharField(max_length=200)
    topic = models.CharField(max_length=200)
    day = models.CharField(max_length=10)
    date = models.DateTimeField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    speaker_name = models.CharField(max_length=100)

    def __str__(self):
        return self.topic


class Participant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    event = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Register(models.Model):
    def __str__(self):
        return self


class SpeakerDetail(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()
    photo = models.ImageField(upload_to="images/")
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    linkedin_link = models.URLField()
    twitter_link = models.URLField()
    event_1 = models.CharField(max_length=100, null=True)
    event_2 = models.CharField(max_length=100, null=True)
    event_3 = models.CharField(max_length=100, null=True)
    rating = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.name
