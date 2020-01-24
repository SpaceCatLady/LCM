from django import forms
from datetime import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from dlcm3.models import Medication, Unit, Severity, YesNoAnswer
    
class MedLogForm(forms.Form):

    med_time = forms.SplitDateTimeField(
        help_text="Select date and time.",
        initial = datetime.now)
    med_id = forms.ModelChoiceField(
        queryset=Medication.objects.all())
    med_dose = forms.DecimalField(
        max_digits = 6,
        decimal_places = 2,
        )
    med_dose_unit = forms.ModelChoiceField(
        queryset = Unit.objects.all()
        )
    med_comment = forms.CharField(
        max_length = 50,
        required = False)

class MoodLogForm(forms.Form):

    mood_date = forms.DateField(
        initial = datetime.today,
        help_text = 'Select Date',
        )
    sleep_hours = forms.DecimalField(
        max_digits = 4,
        decimal_places = 2,
        help_text = 'Enter hours slept')

    weight = forms.DecimalField(
        max_digits = 5,
        decimal_places = 2,
        help_text = 'Enter your weight',
        required = False,
        )
    bp_phase = forms.ModelChoiceField(
        queryset = Severity.objects.all(),
        help_text = 'Select bipolar phase',
        label = 'Bipolar Phase',
        initial = 5)
    mood_score = forms.IntegerField(
        help_text = 'Enter a score between 0 and 100',
        )
    other_symp = forms.CharField(
        max_length = 300,
        required = False,
        label = 'Other psychological symptoms')
    period = forms.ModelChoiceField(
        queryset = YesNoAnswer.objects.all(),
        required = False)
    msw_count = forms.IntegerField(
        required = False,
        label = 'Number of mood swings')
    life_event = forms.CharField(
        max_length = 50,
        required = False)
    life_event_effect = forms.IntegerField(
        required = False,
        label = 'Effect of event on mood score between -4 and 4',)
    hosp_adm = forms.BooleanField(
        required = False,
        initial = False,
        label = 'Admitted to hospital')

    class Meta:
        unique_together = [['user_id', 'mood_date']]

    def get_absolute_url(self):
        return reverse('mood-log', args = [str(self.id)])

    def __str__(self):
        return f'{self.user}{self.mood_date,} {self.bp_phase} {self.other_symp} {self.mood_score} {self.msw_count} {self.life_event}{self.life_event_effect} {self.hosp_adm} {self.weight} {self.sleep_hours} {self.period}'
