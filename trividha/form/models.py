from django.db import models

# Create your models here.
class school(models.Model):
    name=models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

class basic_details(models.Model):
    school=models.OneToOneField(school,on_delete=models.CASCADE,default=1)
    participants_number=models.IntegerField()
    staff_number=models.IntegerField()
    veg=models.IntegerField()
    non_veg=models.IntegerField()

    def __str__(self):
        return self.school.name

class main_events(models.Model):
    name=models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    

class events(models.Model):
    name=models.CharField(max_length=30)
    host=models.ForeignKey(main_events, on_delete=models.CASCADE,default=1)
    is_team_event = models.BooleanField(default=False)
    max_team_size = models.PositiveIntegerField(null=True, blank=True)
    max_teams_per_school = models.PositiveIntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.name


class participant_details(models.Model):
    name=models.CharField(max_length=30)
    school=models.ForeignKey(school, on_delete=models.CASCADE)
    events=models.ForeignKey(events, on_delete=models.CASCADE)

    def __str__(self):
        return self.school.name