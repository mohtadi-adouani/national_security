from typing import Any
from django.db import models
from django.utils.crypto import get_random_string

class PreRequestIDCManager(models.Manager):
    def create(self, **kwargs: Any) -> Any:
        __idcpr =  self.model(**kwargs) # create identity card pre request
        __idcpr.number = get_random_string(length=12) # generate number
        __idcpr.save()  # save object
        return __idcpr

class PreRequestPassportManager(models.Manager):
    def create(self, **kwargs: Any) -> Any:
        __passport_pr =  self.model(**kwargs) # create passport pre request
        __passport_pr.number = get_random_string(length=12) # generate number
        __passport_pr.save()  # save object
        return __passport_pr
