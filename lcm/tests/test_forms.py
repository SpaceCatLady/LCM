from datetime import *

from django.test import TestCase

from dlcm3.models import Medication, Unit, Severity, YesNoAnswer
from dlcm3.forms import MedLogForm, MoodLogForm

class MedLogFormTest(TestCase):

    def test_medlogform_med_time_help_text(self):
        form = MedLogForm()
        self.assertEqual(form.fields['med_time'].help_text, 'Select date and time.')

    def test_medlogform_med_time_help_text(self):
        form = MedLogForm()
        self.assertEqual(form.fields['med_time'].initial, datetime.now)

    def test_medlogform_med_id_queryset(self):
        form = MedLogForm()
        queryset = Medication.objects.all() 
        self.assertQuerysetEqual(form.fields['med_id'].queryset, queryset)

    def test_medlogform_med_dose_unit_queryset(self):
        form = MedLogForm()
        queryset = Unit.objects.all() 
        self.assertQuerysetEqual(form.fields['med_dose_unit'].queryset, queryset)

    def test_medlogform_med_dose_max_digits(self):
        form = MedLogForm()
        self.assertEqual(form.fields['med_dose'].max_digits, 6)

    def test_medlogform_med_dose_decimal_places(self):
        form = MedLogForm()
        self.assertEqual(form.fields['med_dose'].decimal_places, 2)

    def test_medlogform_med_comment_max_length(self):
        form = MedLogForm()
        self.assertEqual(form.fields['med_comment'].max_length, 50)

class MoodLogFormTest(TestCase):

    def test_moodlogform_mood_date_help_text(self):
        form = MoodLogForm()
        self.assertEqual(form.fields['mood_date'].help_text, 'Select date')

    def test_moodlogform_mood_date_initial(self):
        form = MoodLogForm()
        self.assertEqual(form.fields['mood_date'].initial, datetime.today)

    def test_moodlogform_sleep_hours_max_digits(self):
        form = MoodLogForm()
        self.assertEqual(form.fields['sleep_hours'].max_digits, 4)

    def test_moodlogform_sleep_hours_decimal_places(self):
        form = MoodLogForm()
        self.assertEqual(form.fields['sleep_hours'].decimal_places, 2)

    def test_moodlogform_sleep_hours_help_text(self):
        form = MoodLogForm()
        self.assertEqual(form.fields['sleep_hours'].help_text, 'Enter hours slept')

    def test_moodlogform_weight_max_digits(self):
        form = MoodLogForm()
        self.assertEqual(form.fields['weight'].max_digits, 5)

    def test_moodlogform_weight_decimal_places(self):
        form = MoodLogForm()
        self.assertEqual(form.fields['weight'].decimal_places, 2)

    def test_moodlogform_weight_decimal_places(self):
        form = MoodLogForm()
        self.assertEqual(form.fields['weight'].required, False)

    def test_moodlogform_weight_help_text(self):
        form = MoodLogForm()
        self.assertEqual(form.fields['weight'].help_text, 'Enter your weight')

    def test_moodlogform_bp_phase_queryset(self):
        form = MoodLogForm()
        queryset = Severity.objects.all() 
        self.assertQuerysetEqual(form.fields['bp_phase'].queryset, queryset)

    def test_moodlogform_bp_phase_help_text(self):
        form = MoodLogForm()
        self.assertEqual(form.fields['bp_phase'].help_text, 'Select bipolar phase')

    def test_moodlogform_bp_phase_label(self):
        form = MoodLogForm()
        self.assertEqual(form.fields['bp_phase'].label, 'Bipolar Phase')

    def test_moodlogform_bp_phase_initial(self):
        form = MoodLogForm()
        self.assertEqual(form.fields['bp_phase'].initial, 5)

    def test_moodlogform_mood_score_help_text(self):
        form = MoodLogForm()
        self.assertEqual(form.fields['mood_score'].help_text, 'Enter a score between 0 and 100')

    def test_moodlogform_other_symp_max_length(self):
        form = MoodLogForm()
        self.assertEqual(form.fields['other_symp'].max_length, 300)

    def test_moodlogform_other_symp_required(self):
        form = MoodLogForm()
        self.assertEqual(form.fields['other_symp'].required, False)

    def test_moodlogform_other_symp_label(self):
        form = MoodLogForm()
        self.assertEqual(form.fields['other_symp'].label, 'Other psychological symptoms')

    def test_moodlogform_period_queryset(self):
        form = MoodLogForm()
        queryset = YesNoAnswer.objects.all() 
        self.assertQuerysetEqual(form.fields['period'].queryset, queryset)

    def test_moodlogform_period_required(self):
        form = MoodLogForm()
        self.assertEqual(form.fields['period'].required, False)

    def test_moodlogform_msw_count_required(self):
        form = MoodLogForm()
        self.assertEqual(form.fields['msw_count'].required, False)

    def test_moodlogform_msw_count_label(self):
        form = MoodLogForm()
        self.assertEqual(form.fields['msw_count'].label, 'Number of mood swings')

    def test_moodlogform_life_event_max_length(self):
        form = MoodLogForm()
        self.assertEqual(form.fields['life_event'].max_length, 50)

    def test_moodlogform_life_event_required(self):
        form = MoodLogForm()
        self.assertEqual(form.fields['life_event'].required, False)

    def test_moodlogform_life_event_effect_required(self):
        form = MoodLogForm()
        self.assertEqual(form.fields['life_event_effect'].required, False)

    def test_moodlogform_life_event_effect_label(self):
        form = MoodLogForm()
        self.assertEqual(form.fields['life_event_effect'].label, 'Effect of event on mood score between -4 and 4')

    def test_moodlogform_hosp_adm_required(self):
        form = MoodLogForm()
        self.assertEqual(form.fields['hosp_adm'].required, False)

    def test_moodlogform_hosp_adm_initial(self):
        form = MoodLogForm()
        self.assertEqual(form.fields['hosp_adm'].initial, False)

    def test_moodlogform_hosp_adm_label(self):
        form = MoodLogForm()
        self.assertEqual(form.fields['hosp_adm'].label, 'Admitted to hospital')

    def test_moodlogform_date_today(self):
        date = datetime.today()
        Severity.objects.create(name = 'Baseline')
        bp_phase = Severity.objects.get(id = 1)
        form = MoodLogForm(data={'mood_date': date, 'sleep_hours': 5.00, 'mood_score': 50, 'bp_phase': bp_phase})
        self.assertTrue(form.is_valid())