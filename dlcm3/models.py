from django.db import models
from django.urls import reverse  # To generate URLS by reversing URL patterns
from django.contrib.auth.models import User
from datetime import date


# Create your models here.

class Medication(models.Model):
    name = models.CharField(
        max_length = 50,
        verbose_name = 'Medication name',)
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE)

    class Meta:
        unique_together = [['name', 'user_id']]
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        #Returns the url to access a particular log entry
        return reverse('med-detail', args=[str(self.id)])

class Unit(models.Model):
    name = models.CharField(
        max_length = 25,
        verbose_name = 'Medication units')
    def __str__(self):
        return self.name

class YesNoAnswer(models.Model):
    code = models.CharField(
        max_length = 5)
    desc = models.CharField(
        max_length = 20)
    def __str__(self):
        #String for representing the Model object.
        return f'{self.code}'

class MedLog(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE)
    med_time = models.DateTimeField(
        help_text = 'Enter date and time of intake',
        default=date.today)
    med_id = models.ForeignKey(
        Medication,
        help_text = 'Please select medication',
        on_delete=models.CASCADE)
    med_dose = models.DecimalField(
        max_digits = 6,
        decimal_places = 2,
        )
    med_dose_unit = models.ForeignKey(
        Unit,
        help_text = 'Choose dosage units',
        on_delete=models.CASCADE)
    med_comment = models.CharField(
        max_length = 50,
        blank = True)

    class Meta:
        # order returned records ascending by med_time 
        ordering = ['-med_time']
        permissions = (("can_enter_med_log", "Enter med log entry"),)

    def get_absolute_url(self):
        #Returns the url to access a particular log entry
        return reverse('med-log-detail', args=[str(self.id)])

    def __str__(self):
        #String for representing the Model object.
        return f'{self.user} {self.med_time} {self.med_dose} {self.med_id.name} {self.med_dose_unit.name} {self.med_comment}'

class Severity(models.Model):
    name = models.CharField(
        max_length = 20
        )
    description = models.CharField(
        max_length = 300,
        blank = True
        )
    def get_abosulte_url(self):
        # returns a url to access a particular log entry
        return reverse('severity', args = [str(self.id)])

    def __str__(self):
        #String for representing the Model object.
        return f'{self.name}'

class MoodLog(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,)

    mood_date = models.DateField(
        default = date.today,
        help_text = 'Select Date',
        )
    bp_phase = models.ForeignKey(
        Severity,
        help_text = 'Select bipolar phase',
        verbose_name = 'Bipolar Phase',
        on_delete=models.CASCADE,
        default = 5)
    other_symp = models.CharField(
        max_length = 300,
        blank = True)
    mood_score = models.IntegerField(
        help_text = 'Enter a score between 0 and 100',
        )
    msw_count = models.IntegerField(
        blank = True,
        null = True,
        verbose_name = 'Number of mood swings')
    life_event = models.CharField(
        max_length = 50,
        blank = True)
    life_event_effect = models.IntegerField(
        blank = True,
        verbose_name = 'Effect of event on mood score between -4 and 4',
        null = True)
    hosp_adm = models.BooleanField(
        blank = True,
        default = False,
        verbose_name = 'Admitted to hospital')
    weight = models.DecimalField(
        max_digits = 5,
        decimal_places = 2,
        help_text = 'Enter your weight',
        blank = True,
        null = True)
    sleep_hours = models.DecimalField(
        max_digits = 4,
        decimal_places = 2,
        help_text = 'Enter hours slept')
    period = models.CharField(
        max_length = 5,
        blank = True,
        null = True)

    class Meta:
        unique_together = [['user_id', 'mood_date']]
        ordering = ['-mood_date']

    def get_absolute_url(self):
        return reverse('mood-log-detail', args = [str(self.id)])

    def __str__(self):
        return f'{self.user}{self.mood_date,} {self.bp_phase} {self.other_symp} {self.mood_score} {self.msw_count} {self.life_event}{self.life_event_effect} {self.hosp_adm} {self.weight} {self.sleep_hours} {self.period}'

