from typing import Any
from django.db import models
from django.utils.crypto import get_random_string
import datetime

class IdentityCardManager(models.Manager):
    def create(self, **kwargs: Any) -> Any:
        __idc =  self.model(**kwargs) # create identity card
        __idc.number = get_random_string(length=12) # generate number
        # generate expiray date
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
        
        

