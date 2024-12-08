from celery import shared_task
from .models import PreRequestIDC, PreRequestPassport
from django.apps import apps

@shared_task
def create_identity_card(idc_pre_req_pk):
    idc_pre_req = PreRequestIDC.objects.get(pk=idc_pre_req_pk)
    IdentityCard = apps.get_model('identity_card', 'IdentityCard')
    identity_card = IdentityCard.objects.create_from_pre_request(pre_request=idc_pre_req)
    idc_pre_req.identity_card = identity_card
    idc_pre_req.save()
    print_identity_card.delay(identity_card.pk)

@shared_task
def print_identity_card(idc_pk):
    """ Simulate printing process"""
    IdentityCard = apps.get_model('identity_card', 'IdentityCard')
    idc = IdentityCard.objects.get(pk=idc_pk)
    print("Printing identity card number", idc.number)
    return idc


@shared_task
def create_passport(passport_pre_req_pk):
    passport_pre_req = PreRequestPassport.objects.get(pk=passport_pre_req_pk)
    Passport = apps.get_model('identity_card', 'Passport')
    passport = Passport.objects.create_from_pre_request(pre_request=passport_pre_req)
    passport_pre_req.passport = passport
    passport_pre_req.save()
    print_passport.delay(passport.pk)

@shared_task
def print_passport(passport_pk):
    """ Simulate printing process"""
    Passport = apps.get_model('identity_card', 'Passport')
    passport = Passport.objects.get(pk=passport_pk)
    print("Printing passport number", passport.number)
    return passport