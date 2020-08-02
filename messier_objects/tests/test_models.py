from django.test import TestCase

from messier_objects.models import MessierObject


class TestModelMessierObject(TestCase):

    def setUp(self):
        # Messier object with just messier_number
        self.mes_object_test_one = MessierObject.objects.create(
            messier_number=1
        )
        # Messier object with messier_number and name
        self.mes_object_test_two = MessierObject.objects.create(
            messier_number=2,
            name='test'
        )

    def test_object_str_return_messier_number_only(self):
        self.assertEquals(self.mes_object_test_one.__str__(),
                          'M' +
                          str(self.mes_object_test_one.messier_number))

    def test_object_str_return_messier_number_and_name(self):
        self.assertEquals(self.mes_object_test_two.__str__(),
                          'M' +
                          str(self.mes_object_test_two.messier_number) +
                          ': ' +
                          self.mes_object_test_two.name)
