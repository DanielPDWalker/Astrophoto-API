from django.test import TestCase

from solar_system_objects.models import SolarSystemObject


class TestModelSolarSystemObject(TestCase):

    def setUp(self):
        self.sol_object_test_one = SolarSystemObject.objects.create(
            name='test1'
        )
        # sol two, same name and data as one, to test unique slug
        self.sol_object_test_two = SolarSystemObject.objects.create(
            name='test1'
        )

    def test_object_is_assigned_unique_slug_on_creation(self):
        self.assertEquals(self.sol_object_test_one.slug,
                          'test1')

    def test_objects_with_same_names_has_unique_slugs(self):
        self.assertNotEquals(self.sol_object_test_one.slug,
                             self.sol_object_test_two.slug)

    def test_object_str_return_name(self):
        self.assertEquals(self.sol_object_test_one.__str__(),
                          self.sol_object_test_one.name)
