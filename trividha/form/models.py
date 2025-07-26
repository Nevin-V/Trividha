from django.db import models

# Create your models here.
class school(models.Model):
    name=models.CharField(max_length=30)

class basic_details(models.Model):
    school=models.OneToOneField(school,on_delete=models.CASCADE)
    participants_number=models.IntegerField()
    staff_number=models.IntegerField()
    veg=models.IntegerField()
    non_veg=models.IntegerField()


class main_events(models.Model):
    name=models.CharField(max_length=30)
    

class events(models.Model):
    name=models.CharField(max_length=30)
    host=models.ForeignKey(main_events, on_delete=models.CASCADE)
    is_team_event = models.BooleanField(default=False)
    max_team_size = models.PositiveIntegerField(null=True, blank=True)
    max_teams_per_school = models.PositiveIntegerField(null=True, blank=True)


class participant_details(models.Model):
    name=models.CharField(max_length=30)
    school=models.ForeignKey(school, on_delete=models.CASCADE)
    events=models.ForeignKey(events, on_delete=models.CASCADE)