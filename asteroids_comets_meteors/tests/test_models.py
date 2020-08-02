from django.test import TestCase

from asteroids_comets_meteors.models import AsteroidCometMeteorObject


class TestModelAsteroidCometMeteorObject(TestCase):

    def setUp(self):
        self.acm_object_test_one = AsteroidCometMeteorObject.objects.create(
            name='test1',
            scientific_name='test1',
            object_type='test1',
            size_km=0
        )
        # acm two, same name and data as one, to test unique slug
        self.acm_object_test_two = AsteroidCometMeteorObject.objects.create(
            name='test1',
            scientific_name='test1',
            object_type='test1',
            size_km=0
        )
        # acm three is to test __str__ return with no name field.
        self.acm_object_test_three = AsteroidCometMeteorObject.objects.create(
            scientific_name='test1',
            object_type='test1',
            size_km=0
        )

    def test_object_is_assigned_unique_slug_on_creation(self):
        self.assertEquals(self.acm_object_test_one.slug,
                          'test1')

    def test_objects_with_same_names_has_unique_slugs(self):
        self.assertNotEquals(self.acm_object_test_one.slug,
                             self.acm_object_test_two.slug)

    def test_object_str_return_name_and_scientific_name(self):
        self.assertEquals(self.acm_object_test_one.__str__(),
                          self.acm_object_test_one.name + ' Scientific Name: ' +
                          self.acm_object_test_one.scientific_name)

    def test_object_str_return_scientific_name_only(self):
        self.assertEquals(self.acm_object_test_three.__str__(),
                          self.acm_object_test_three.scientific_name)
