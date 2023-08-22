from django.db import models

# Create your models here.
class Identity(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

class furniture_complain(models.Model):
    name = models.CharField(max_length=100)
    category = models.TextField()
    reason = models.TextField()
    damage = models.TextField()

    def __str__(self):
        return self.name
