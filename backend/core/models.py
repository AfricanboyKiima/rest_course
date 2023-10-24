from django.db import models
from utils.model_abstracts import Model
from django_extensions.db.models import (TimeStampedModel,ActivatorModel,TitleDescriptionModel)

class Contact(TimeStampedModel,ActivatorModel,TitleDescriptionModel):
    """
    -TimeStampModel provides us with the created field to help us know when something was created
    -ActivatorModel helps us with the status field to know the activated and deactivated date 
    -TitleDescriptionModel helps us with two character fields
    """
    email = models.EmailField(verbose_name = "Email")


    class Meta:
        verbose_name_plural = "Contacts"

    def __str__(self):
        return f'{self.title}'

