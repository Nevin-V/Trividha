from django.db import models
import datetime

# Create your models here.
class details(models.Model):
    date=models.DateField()
    inaugartion_time=models.TextField(null=True)
    chief_guest_name=models.TextField(null=True)
    events_time=models.TextField(default="11.00am-4.30pm")
    logo=models.ImageField(null=True,upload_to="images/")
    sthithapragya=models.ImageField(null=True,upload_to="images/")
    optazia=models.ImageField(null=True,upload_to="images/")
    xenora=models.ImageField(null=True,upload_to="images/")
    main_poster=models.ImageField(null=True,upload_to="images/")
    inaugration_poster=models.ImageField(null=True,upload_to="images/")
    chief_guest_poster=models.ImageField(null=True,upload_to="images/")

    def __str__(self):
        return "Trividha Website Layout"

    

