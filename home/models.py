from django.db import models

# Create your models here.



class Event_Participant(models.Model):
    name = models.CharField(("Name"), max_length=50)
    email = models.CharField(("Email"), max_length=50)
    teamname = models.CharField(("Team Name"), max_length=50)
    phone = models.CharField(("Phone"), max_length=50)
    collegename = models.CharField(("College Name"), max_length=50)
    event = models.CharField(("Event Name"), max_length=50)


    def __str__(self):
        return f'Name {self.name} - Event {self.event}'
    