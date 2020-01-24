from django.test import TestCase
from django.contrib.auth.models import User

from dlcm3.models import Medication



class MedicationModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # create test user
        my_user = User.objects.create(username='User01')
        # Set up non-modified objects used by all test methods
        Medication.objects.create(name='Olanzapine', user_id=my_user)

    def test_name_label(self):
        medication = Medication.objects.get(id=1)
        field_label = medication._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Medication name')

    def test_name_max_length(self):
        medication = Medication.objects.get(id=1)
        max_length = medication._meta.get_field('name').max_length
        self.assertEquals(max_length, 50)

    def test_object_name_is_name(self):
        medication = Medication.objects.get(id=1)
        expected_object_name = f'{medication.name}'
        self.assertEquals(expected_object_name, str(medication))

    def test_get_absolute_url(self):
        medication = Medication.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(medication.get_absolute_url(), '/dlcm3/meds/1')