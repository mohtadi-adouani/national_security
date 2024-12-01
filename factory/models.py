from django.db import models
from django.contrib.auth.models import User
from identity_card.models import SEXE
from .managers import PreRequestIDCManager
from datetime import datetime

class PreRequestIDC(models.Model):
    # identity
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    sexe = models.CharField(
        max_length=1,
        choices=SEXE,
        default=list(SEXE.keys())[0]
    )
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=50)
    adress = models.CharField(max_length=65)
    # idc pr info
    author = models.ForeignKey(User, related_name='pre_request_idc_author', 
                               on_delete=models.SET_NULL, blank=True, null=True)
    corrector = models.ForeignKey(User, related_name='pre_request_idc_corrector',
                                  on_delete=models.SET_NULL, blank=True, null=True)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    number = models.CharField(max_length=12, blank=True)
    validation = models.DateTimeField(null=True, blank=True) # corrector validated idc

    objects = PreRequestIDCManager()
    def __str__(self) -> str:
        return f"Pre-Request-IDC {self.number}"
    
    def validate(self, corrector: User):
        """ add corrector and set validation datetime"""
        self.corrector = corrector
        self.validation = datetime.now()
        self.save()