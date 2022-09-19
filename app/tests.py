from django.test import TestCase
from .models import Carro
from django.db import models
from django.urls import resolve,reverse
from .views import create,update

class TestModel(TestCase):

    def test_should_create_carro(self):
        carro = Carro.objects.create(nome='fiat',marca='fiat',cor='vermelho')
        carro.save()

        self.assertEqual(str(carro),'fiat')

class testUrls(TestCase):
    
    def test_create_url_is_resolved(self):
        url = reverse('create')

        self.assertEquals(resolve(url).func, create)
        self.assertEquals(resolve(url).route,'create/')
