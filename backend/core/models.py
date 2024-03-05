from django.db import models
from utils.model_abstracts import Model
from django_extensions.db.models import TimeStampedModel,ActivatorModel,TitleDescriptionModel

class Contact(TimeStampedModel,ActivatorModel,TitleDescriptionModel,Model):
    """
    -TimeStampModel - adds created and modified fields to our model
    -ActivatorModel - adds is_active and activated_date fields to our models
    -TitleDescriptionModel - adds title and Description fields to our models
    """
    email = models.EmailField(verbose_name = "Email")


    class Meta:#class provides us with additional information about our data(object(contact)), in this case on our contact data
        verbose_name_plural = "Contacts"

    def __str__(self):
        return f'{self.title}'