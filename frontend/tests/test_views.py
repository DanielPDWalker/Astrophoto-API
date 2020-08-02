import json
from django.test import TestCase, Client
from django.urls import reverse

from asteroids_comets_meteors.models import AsteroidCometMeteorObject
from messier_objects.models import MessierObject
from solar_system_objects.models import SolarSystemObject


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

        # Messier Object Set Up
        self.mes_overview_url = reverse('mes_obj_overview')
        self.messier_obj_test = MessierObject.objects.create(
            messier_number=1000000,
            name='test1000000',
            ncg_or_ic_number=1000000,
            object_type='Test',
            distance_kly=25,
            constellation='Test',
            apparent_magnitude=1000000,
        )
        self.mes_detail_url = reverse('mes_obj_detail', args=[
                                      self.messier_obj_test.messier_number])

        # Solar System Object Set Up
        self.sol_overview_url = reverse('sol_obj_overview')
        self.sol_obj_test = SolarSystemObject.objects.create(
            name='test',
            object_type='test',
            parent_object='test',
            distance_from_sun_au=0,
        )
        self.sol_detail_url = reverse('sol_obj_detail', args=[
                                      self.sol_obj_test.slug])

        # Asteroid Comet Meteors Object Set Up
        self.acm_overview_url = reverse('acm_obj_overview')
        self.acm_obj_test = AsteroidCometMeteorObject.objects.create(
            scientific_name='test'
        )
        self.acm_detail_url = reverse('acm_obj_detail', args=[
            self.acm_obj_test.slug])

    def test_mes_obj_overview_get(self):
        response = self.client.get(self.mes_overview_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'api_frontends/messier_objects_overview.html')

    def test_mes_obj_detail_get(self):
        response = self.client.get(self.mes_detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'api_frontends/messier_object_detail.html')

    def test_sol_obj_overview_get(self):
        response = self.client.get(self.sol_overview_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'api_frontends/solar_system_objects_overview.html')

    def test_sol_obj_detail_get(self):
        response = self.client.get(self.sol_detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'api_frontends/solar_system_object_detail.html')

    def test_acm_obj_overview_get(self):
        response = self.client.get(self.acm_overview_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'api_frontends/asteroids_comets_meteors_overview.html')

    def test_acm_obj_detail_get(self):
        response = self.client.get(self.acm_detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'api_frontends/asteroids_comets_meteors_detail.html')
