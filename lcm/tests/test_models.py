import datetime
import pytz

from django.test import TestCase
from django.contrib.auth.models import User
from django.db import IntegrityError

from dlcm3.models import Medication, Unit, MedLog, Severity, MoodLog

class MedicationModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # create test user
        my_user = User.objects.create(username='User01')
        print('--------------------------------------')
        print("Test user created for model testing.")
        print('--------------------------------------')
        # Set up non-modified objects used by all test methods
        Medication.objects.create(name='Olanzapine', user_id=my_user)

    def test_med_unique_together(self):
        my_user = User.objects.get(id=1)
        
        with self.assertRaises(IntegrityError):
            Medication.objects.create(name='Olanzapine', user_id=my_user)
    
    def test_med_name_label(self):
        medication = Medication.objects.get(id=1)
        field_label = medication._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Medication name')

    def test_med_name_max_length(self):
        medication = Medication.objects.get(id=1)
        max_length = medication._meta.get_field('name').max_length
        self.assertEquals(max_length, 50)



class UnitModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Unit.objects.create(name='Milligram(s)')

    def test_unit_name_label(self):
        unit = Unit.objects.get(id=1)
        field_label = unit._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Medication units')

    def test_unit_name_max_length(self):
        unit = Unit.objects.get(id=1)
        max_length = unit._meta.get_field('name').max_length
        self.assertEquals(max_length, 25)

    def test_unit_object_name_is_name(self):
        unit = Unit.objects.get(id=1)
        expected_object_name = f'{unit.name}'
        self.assertEquals(expected_object_name, str(unit))


class MoodLogModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(username='User01')
        Severity.objects.create(name='Stable')
        
        severity = Severity.objects.get(id=1)
        my_user = User.objects.get(id=1)
        # Set up non-modified objects used by all test methods
        MoodLog.objects.create(
            user = my_user, 
            mood_date = '2020-01-31',
            bp_phase = severity,
            mood_score = 50,
            sleep_hours = 8)
        print('--------------------------------------')
        print("Test data created for testing models.")
        print('--------------------------------------')      
    def test_moodlog_mood_date_helptext(self):
        moodlog = MoodLog.objects.get(id=1)
        field_helptext= moodlog._meta.get_field('mood_date').help_text
        self.assertEquals(field_helptext, 'Select Date')
    
    def test_moodlog_bp_phase_helptext(self):
        moodlog = MoodLog.objects.get(id=1)
        field_helptext= moodlog._meta.get_field('bp_phase').help_text
        self.assertEquals(field_helptext, 'Select bipolar phase')

    def test_moodlog_bp_phase_verbose_name(self):
        moodlog = MoodLog.objects.get(id=1)
        field_verbose_name= moodlog._meta.get_field('bp_phase').verbose_name
        self.assertEquals(field_verbose_name, 'Bipolar Phase')

    def test_moodlog_bp_phase_default(self):
        moodlog = MoodLog.objects.get(id=1)
        field_default= moodlog._meta.get_field('bp_phase').default
        self.assertEquals(field_default, 5)

    def test_moodlog_other_symp_max_length(self):
        moodlog = MoodLog.objects.get(id=1)
        max_length= moodlog._meta.get_field('other_symp').max_length
        self.assertEquals(max_length, 300)

    def test_moodlog_mood_score_helptext(self):
        moodlog = MoodLog.objects.get(id=1)
        field_helptext= moodlog._meta.get_field('mood_score').help_text
        self.assertEquals(field_helptext, 'Enter a score between 0 and 100')

    def test_moodlog_msw_count_verbose_name(self):
        moodlog = MoodLog.objects.get(id=1)
        field_verbose_name= moodlog._meta.get_field('msw_count').verbose_name
        self.assertEquals(field_verbose_name, 'Number of mood swings')

    def test_moodlog_life_event_max_length(self):
        moodlog = MoodLog.objects.get(id=1)
        max_length= moodlog._meta.get_field('life_event').max_length
        self.assertEquals(max_length, 50)
    
    def test_moodlog_life_event_effect_verbose_name(self):
        moodlog = MoodLog.objects.get(id=1)
        field_verbose_name= moodlog._meta.get_field('life_event_effect').verbose_name
        self.assertEquals(field_verbose_name, 'Effect of event on mood score between -4 and 4')

    def test_moodlog_hosp_adm_verbose_name(self):
        moodlog = MoodLog.objects.get(id=1)
        field_verbose_name= moodlog._meta.get_field('hosp_adm').verbose_name
        self.assertEquals(field_verbose_name, 'Admitted to hospital')

    def test_moodlog_weight_max_digits(self):
        moodlog = MoodLog.objects.get(id=1)
        max_digits= moodlog._meta.get_field('weight').max_digits
        self.assertEquals(max_digits, 5)

    def test_moodlog_weight_decimal_places(self):
        moodlog = MoodLog.objects.get(id=1)
        decimal_places= moodlog._meta.get_field('weight').decimal_places
        self.assertEquals(decimal_places, 2)

    def test_moodlog_weight_helptext(self):
        moodlog = MoodLog.objects.get(id=1)
        field_helptext= moodlog._meta.get_field('weight').help_text
        self.assertEquals(field_helptext, 'Enter your weight')

    def test_moodlog_sleep_hours_max_digits(self):
        moodlog = MoodLog.objects.get(id=1)
        max_digits= moodlog._meta.get_field('sleep_hours').max_digits
        self.assertEquals(max_digits, 4)

    def test_moodlog_sleep_hours_decimal_places(self):
        moodlog = MoodLog.objects.get(id=1)
        decimal_places= moodlog._meta.get_field('sleep_hours').decimal_places
        self.assertEquals(decimal_places, 2)

    def test_moodlog_sleep_hours_helptext(self):
        moodlog = MoodLog.objects.get(id=1)
        field_helptext= moodlog._meta.get_field('sleep_hours').help_text
        self.assertEquals(field_helptext, 'Enter hours slept')

    def test_moodlog_period_max_length(self):
        moodlog = MoodLog.objects.get(id=1)
        max_length= moodlog._meta.get_field('period').max_length
        self.assertEquals(max_length, 5)

    def test_medlog_object_name(self):
        moodlog = MoodLog.objects.get(id=1)
        expected_object_name = f'{moodlog.user}{moodlog.mood_date,} {moodlog.bp_phase} {moodlog.other_symp} {moodlog.mood_score} {moodlog.msw_count} {moodlog.life_event}{moodlog.life_event_effect} {moodlog.hosp_adm} {moodlog.weight} {moodlog.sleep_hours} {moodlog.period}'
        self.assertEquals(expected_object_name, str(moodlog))

    def test_medlog_get_absolute_url(self):
        moodlog = MoodLog.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(moodlog.get_absolute_url(), '/dlcm3/moodlog/1')

class MedLogModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(username ='User01')
        my_user = User.objects.get(id = 1)

        Medication.objects.create(name = 'Medication01', user_id = my_user)
        Unit.objects.create(name = 'Milligram(s)') 
        
        # Set up non-modified objects used by all test methods
        med = Medication.objects.get(id = 1)
        unit = Unit.objects.get(id = 1)
        med_time = datetime.datetime(2020, 1, 31, 21, 0, 0, 0, tzinfo=pytz.UTC)

        MedLog.objects.create(
            user = my_user,
            med_time = med_time, 
            med_id = med,
            med_dose= 1,
            med_dose_unit = unit)
        print('--------------------------------------')
        print('Test data created for tesing of models.')
        print('--------------------------------------')

    def test_medlog_med_time_helptext(self):
        medlog = MedLog.objects.get(id = 1)
        field_helptext= medlog._meta.get_field('med_time').help_text
        self.assertEquals(field_helptext, 'Enter date and time of intake')
    
    def test_medlog_med_time_default(self):
        medlog = MedLog.objects.get(id=1)
        field_default= medlog._meta.get_field('med_time').default
        self.assertEquals(field_default, datetime.date.today)

    def test_medlog_med_id_helptext(self):
        medlog = MedLog.objects.get(id=1)
        field_helptext= medlog._meta.get_field('med_id').help_text
        self.assertEquals(field_helptext, 'Please select medication')

    def test_medlog_med_dose_max_digits(self):
        medlog = MedLog.objects.get(id=1)
        max_digits= medlog._meta.get_field('med_dose').max_digits
        self.assertEquals(max_digits, 6)

    def test_medlog_med_dose_decimal_places(self):
        medlog = MedLog.objects.get(id=1)
        decimal_places= medlog._meta.get_field('med_dose').decimal_places
        self.assertEquals(decimal_places, 2)

    def test_medlog_med_dose_unit_helptext(self):
        medlog = MedLog.objects.get(id=1)
        field_helptext= medlog._meta.get_field('med_dose_unit').help_text
        self.assertEquals(field_helptext, 'Choose dosage units')

    def test_medlog_med_comment_max_length(self):
        medlog = MedLog.objects.get(id=1)
        max_length= medlog._meta.get_field('med_comment').max_length
        self.assertEquals(max_length, 50)

    def test_medlog_object_name(self):
        medlog = MedLog.objects.get(id=1)
        expected_object_name = f'{medlog.user} {medlog.med_time} {medlog.med_dose} {medlog.med_id.name} {medlog.med_dose_unit.name} {medlog.med_comment}'
        self.assertEquals(expected_object_name, str(medlog))

    def test_medlog_get_absolute_url(self):
        medlog = MedLog.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(medlog.get_absolute_url(), '/dlcm3/medlog/1')