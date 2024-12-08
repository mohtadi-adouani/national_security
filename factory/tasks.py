from celery import shared_task
from .models import PreRequestIDC
from django.apps import apps

@shared_task
def create_identity_card(idc_pre_req_pk):
    idc_pre_req = PreRequestIDC.objects.get(pk=idc_pre_req_pk)
    IdentityCard = apps.get_model('identity_card', 'IdentityCard')
    identity_card = IdentityCard.objects.create_from_pre_request(pre_request=idc_pre_req)
    idc_pre_req.identity_card = identity_card
    print_identity_card.delay(identity_card.pk)

@shared_task
def print_identity_card(idc_pk):
    """ Simulate printing process"""
    IdentityCard = apps.get_model('identity_card', 'IdentityCard')
    idc = IdentityCard.objects.get(pk=idc_pk)
    print("Printing identity card number", idc.number)
    return idc