from django.db import models


class Contacts(models.Model):
    contact_name = models.name = models.CharField(max_length=500)
    contact_email = models.name = models.CharField(max_length=500)
