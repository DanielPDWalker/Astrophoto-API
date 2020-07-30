from django.test import SimpleTestCase
from django.urls import reverse, resolve
from frontend.views import mes_obj_overview, mes_obj_detail
from frontend.views import sol_obj_overview, sol_obj_detail
from frontend.views import acm_obj_overview, acm_obj_detail


class TestUrls(SimpleTestCase):

    def test_messier_objects_url_resolves(self):
        url = reverse('mes_obj_overview')
        self.assertEquals(resolve(url).func, mes_obj_overview)

    def test_messier_objects_detail_url_resolves(self):
        # The detail url takes a parameter.
        url = reverse('mes_obj_detail', args=[1])
        self.assertEquals(resolve(url).func, mes_obj_detail)

    def test_solar_system_object_url_resolves(self):
        url = reverse('sol_obj_overview')
        self.assertEquals(resolve(url).func, sol_obj_overview)

    def test_solar_system_object_detail_url_resolves(self):
        # The detail url takes a parameter.
        url = reverse('sol_obj_detail', args=[1])
        self.assertEquals(resolve(url).func, sol_obj_detail)

    def test_acm_object_url_resolves(self):
        url = reverse('acm_obj_overview')
        self.assertEquals(resolve(url).func, acm_obj_overview)

    def test_acm_object_detail_url_resolves(self):
        # The detail url takes a parameter.
        url = reverse('acm_obj_detail', args=[1])
        self.assertEquals(resolve(url).func, acm_obj_detail)
