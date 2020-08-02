from django.test import TestCase
from django.test.client import RequestFactory

from utils.frontend_view_utils import overview_post_request
from solar_system_objects.models import SolarSystemObject


class TestFrontendViewUtils(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.request_mes_obj = self.factory.post('/messier_objects',
                                                 {'captured_only_button':
                                                  'captured_only_button'})
        self.request_acm_obj = self.factory.post('/asteroids_comets_meteors',
                                                 {'not_captured_only_button':
                                                  'not_captured_only_button'})
        self.request_sol_obj = self.factory.post('/solar_system_objects',
                                                 {'reset_filters_button':
                                                  'reset_filters_button'})

    def test_overview_post_request_messier_objects_captured(self):
        self.messier_objects_list = overview_post_request(
            self.request_mes_obj)

        for item in self.messier_objects_list:
            self.assertEquals(item.captured, True)

    def test_overview_post_request_asteroid_comet_meteor_object_not_captured(self):
        self.asteroid_comet_meteor_list = overview_post_request(
            self.request_acm_obj)

        for item in self.asteroid_comet_meteor_list:
            self.assertEquals(item.captured, False)

    def test_overview_post_request_solar_system_objects_reset_filters(self):
        self.solar_system_object_list = overview_post_request(
            self.request_sol_obj)

        self.assertEquals(set(self.solar_system_object_list),
                          set(SolarSystemObject.objects.all()))
