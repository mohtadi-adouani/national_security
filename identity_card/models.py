from django.utils.crypto import get_random_string
from django.db import models
from datetime import datetime, timedelta

class IdentityCard(models.Model):
    __validity_years = 10
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    adress = models.CharField(max_length=65)
    number = models.CharField(max_length=12, default=get_random_string(length=12))
    
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=50)
    
    date_of_creation = models.DateField(auto_now_add=True)
    expiry_date = models.DateField(default=datetime.now() + timedelta(days=__validity_years * 365 -1))

    def __str__(self) -> str:
        return f"{self.first_name} - {self.last_name}"