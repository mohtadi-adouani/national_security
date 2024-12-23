from django.db import models
from .managers import PassportManager, IdentityCardManager

SEXE = {
    'F': "Female",
    'M': "Male",
}
PASSPORT_TYPE = {
'P': 'Personal',
'O': 'Official',
'D': 'Diplomatic',
'E': 'Emergency Travel',
}

EYES_COLOR = {
    0 :'Black',
    1 :'Brown',
    2 :'Hazel',
    3 :'Green',
    4 :'Blue',
    5 :'Grey',
    6 :'A',
}

class IdentityCard(models.Model):
    VALIDITY_YEARS = 10
    IDC_STATUS = {
        False: 'INACTIVE',
        True: 'ACTIVE',
    }
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
    # idc info
    date_of_creation = models.DateField(auto_now_add=True)
    expiry_date = models.DateField(blank=True, null=True)
    number = models.CharField(max_length=12, blank=True)
    status = models.BooleanField(
        choices=IDC_STATUS,
        default=list(IDC_STATUS.keys())[0]
    )

    objects = IdentityCardManager()
    def __str__(self) -> str:
        return f"Identity Card {self.first_name} - {self.last_name}"

    def activate(self):
        self.status = self.IDC_STATUS[True]
    

class Passport(models.Model):
    VALIDITY_YEARS = 10
    PASSPORT_STATUS = {
        False: 'INACTIVE',
        True: 'ACTIVE',
    }
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
    eyes_color = models.IntegerField(
        choices=EYES_COLOR,
        default=list(EYES_COLOR.keys())[0]
    )
    height = models.PositiveIntegerField()
    # passport
    type = models.CharField(
        max_length=1,
        choices=PASSPORT_TYPE,
        default=list(PASSPORT_TYPE.keys())[0]
    )
    date_of_creation = models.DateField(auto_now_add=True)
    expiry_date = models.DateField(blank=True, null=True)
    number = models.CharField(max_length=12, blank=True)
    status = models.BooleanField(
        choices=PASSPORT_STATUS,
        default=list(PASSPORT_STATUS.keys())[0]
    )
    objects = PassportManager()
    def __str__(self) -> str:
        return f"Passport {self.first_name} - {self.last_name}"

    def activate(self):
        self.status = self.PASSPORT_STATUS[True]