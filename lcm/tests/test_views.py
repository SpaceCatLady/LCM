from django.test import TestCase
from django.contrib.auth.models import User
from django.test.client import Client
from django.urls import reverse

from dlcm3.models import Medication, MedLog, Unit

class MedicationistViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 authors for pagination tests
        number_of_meds = 15
        #User.objects.create(username ='User01')
        #my_user = User.objects.get(id = 1)
        my_user = User.objects.create_user('User01', password='Password01')
        my_user.save()  
        print("Test user created")

        for med_id in range(number_of_meds):
            Medication.objects.create(
                name = f'Medication {med_id}',
                user_id = my_user
                )

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('meds'))
        self.assertRedirects(response, '/accounts/login/?next=/dlcm3/meds/')

    def test_view_url_exists_at_desired_location(self):
        self.client.login(username='User01', password='Password01')
        response = self.client.get('/dlcm3/meds/')
        #print(response['location'])
        self.assertEqual(response.status_code, 200)
        

    def test_view_url_accessible_by_name(self):
        self.user = User.objects.create_user('User03', password='Password03')
        self.client.login(username='User03', password='Password03')
        response = self.client.get(reverse('meds'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        self.client.login(username='User01', password='Password01')
        response = self.client.get(reverse('meds'))
        #print(response['location'])
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dlcm3/medication_list.html')
        
    def test_pagination_is_ten(self):
        self.client.login(username='User01', password='Password01')
        response = self.client.get(reverse('meds'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['medication_list']) == 10)

    def test_lists_all_meds(self):
        self.client.login(username='User01', password='Password01')
        # Get second page and confirm it has (exactly) remaining 3 items
        response = self.client.get(reverse('meds') + '?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['medication_list']) == 5)

class MedLogistViewTest(TestCase):
    @classmethod
    def setUpTestData(self):
        # Create 13 authors for pagination tests
        number_of_logs = 25
        #User.objects.create(username ='User01')
        #my_user = User.objects.get(id = 1)
        my_user = User.objects.create_user('User01', password='Password01')
        my_user.save()  
        print("Test user created")

        unit = Unit.objects.create(name = 'Unit1')
        unit.save()
        print("test unit created")

        number_of_meds = 25
        for med_id in range(number_of_meds):
            Medication.objects.create(
                name = f'Medication {med_id}',
                user_id = my_user
                )
            print(f'med {med_id} created')


        for log in range(number_of_logs):
            med = Medication.objects.get(id = + 1 )
            MedLog.objects.create(
                user = my_user,
                med_id = med,
                med_dose = log,
                med_dose_unit = unit,
                )
            print(f'med log {log} created')

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('med-log'))
        self.assertRedirects(response, '/accounts/login/?next=/dlcm3/medlog/')

    def test_view_url_exists_at_desired_location(self):
        self.client.login(username='User01', password='Password01')
        response = self.client.get('/dlcm3/medlog/')
        #print(response['location'])
        self.assertEqual(response.status_code, 200)
        

    def test_view_url_accessible_by_name(self):
        self.client.login(username='User01', password='Password01')
        response = self.client.get(reverse('med-log'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        self.client.login(username='User01', password='Password01')
        response = self.client.get(reverse('med-log'))
        #print(response['location'])
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dlcm3/medlog_list.html')
        
    def test_pagination_is_ten(self):
        self.client.login(username='User01', password='Password01')
        response = self.client.get(reverse('med-log'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['medlog_list']) == 20)

    def test_lists_all_medlogs(self):
        self.client.login(username='User01', password='Password01')
        # Get second page and confirm it has (exactly) remaining 3 items
        response = self.client.get(reverse('med-log') + '?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['medlog_list']) == 5)

class MedDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(self):
        # Create 13 authors for pagination tests
        number_of_logs = 10
        #User.objects.create(username ='User01')
        #my_user = User.objects.get(id = 1)
        my_user = User.objects.create_user('User01', password='Password01')
        my_user.save()  
        print("Test user created")

        unit = Unit.objects.create(name = 'Unit1')
        unit.save()
        print("test unit created")

        number_of_meds = 10       

    def test_redirect_if_not_logged_in(self):
        my_user = User.objects.get(pk = 1)
        self.medication = Medication.objects.create(
            user_id = my_user,
            name='Test medication 01')
        response = self.client.get(reverse('med-detail', kwargs={'pk': self.medication.pk}))
        self.assertRedirects(response, '/accounts/login/?next=/dlcm3/meds/1')

    def test_view_url_exists_at_desired_location(self):
        self.client.login(username='User01', password='Password01')
        my_user = User.objects.get(pk = 1)
        self.medication = Medication.objects.create(
            user_id = my_user,
            name='Test medication 02')
        print("Test medication 02 created")
        response = self.client.get('dlcm3/meds/1')
        print(response)
        self.assertEqual(response.status_code, 200)
        

    def test_view_url_accessible_by_name(self):
        self.client.login(username='User01', password='Password01')
        my_user = User.objects.get(pk = 1)
        self.medication = Medication.objects.create(
            user_id = my_user,
            name='Test medication 03')
        response = self.client.get(reverse('med-detail', kwargs={'pk': self.medication.pk}))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        self.client.login(username='User01', password='Password01')
        my_user = User.objects.get(pk = 1)
        self.medication = Medication.objects.create(
            user_id = my_user,
            name='Test medication 04')
        response = self.client.get(reverse('med-detail', kwargs={'pk': self.medication.pk}))
        #print(response['location'])
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dlcm3/medication_detail.html')
        

