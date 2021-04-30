from django.db import models
from datetime import datetime

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        today_d = datetime.today()
        input = datetime.strptime(postData['release'], '%Y-%m-%d')
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "The title of your show needs to be at least 2 characters long"
        if len(postData['network']) < 3:
            errors['network'] = "The network needs to be at least 3 characters long"
        if today_d < input:
            errors['release'] = "The release date needs to be in the past"        
        if len(postData['desc']) < 10:
            errors['desc'] = "The description needs to be at least 10 characters long"
        return errors


class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release = models.DateField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()


