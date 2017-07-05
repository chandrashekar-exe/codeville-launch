from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class UserDetail(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    phone = PhoneNumberField()
    registered_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.name
