from typing import Any
from django.db import models
from django.utils.crypto import get_random_string
import datetime

class IdentityCardManager(models.Manager):
    def create(self, **kwargs: Any) -> Any:
        __idc =  self.model(**kwargs) # create identity card
        __idc.number = get_random_string(length=12) # generate number
        # generate expiry date
        __date_now = datetime.date.today()
        __idc.date_of_creation = __date_now
        __idc.expiry_date = datetime.date(__date_now.year + self.model.VALIDITY_YEARS,
                                            __date_now.month,
                                            __date_now.day)
        __idc.save()  # save object
        return __idc

    def create_from_pre_request(self, pre_request):
        __idc =  self.model(
            first_name=pre_request.first_name,
            last_name=pre_request.last_name,
            sexe=pre_request.sexe,
            date_of_birth=pre_request.date_of_birth,
            place_of_birth=pre_request.place_of_birth,
            adress=pre_request.adress,
            date_of_creation=pre_request.date_of_creation,
        )
        __idc.number = get_random_string(length=12) # generate number
        # generate expiry date
        __date_now = datetime.date.today()
        __idc.date_of_creation = __date_now
        __idc.expiry_date = datetime.date(__date_now.year + self.model.VALIDITY_YEARS,
                                            __date_now.month,
                                            __date_now.day)
        __idc.save()  # save object
        return __idc



class PassportManager(models.Manager):
    def create(self, **kwargs: Any) -> Any:
        __passport =  self.model(**kwargs) # create passport
        __passport.number = get_random_string(length=12) # generate number
        # generate expiray date
        __date_now = datetime.date.today()
        __passport.date_of_creation = __date_now
        __passport.expiry_date = datetime.date(__date_now.year + __passport.VALIDITY_YEARS,
                                                __date_now.month,
                                                __date_now.day)
        __passport.save()  # save object
        return __passport
        
        

