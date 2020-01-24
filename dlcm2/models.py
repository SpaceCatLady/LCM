from django.db import models
from django.utils import timezone

# Create your models here.

class MedicineLog(models.Model):
    med_date = models.DateField('submission date')
    med_time = models.TimeField('Time of intake', default = timezone.now())
    class MedName(models.TextChoices):
        OLANZAPINE = 'OP'
        LORAZEPAM = 'LP'
    med_name = models.CharField('Name of medicine',choices = MedName.choices, max_length =2)
    med_dose = models.DecimalField('Dosage Taken',max_digits=10, decimal_places = 2)
    class Unit(models.TextChoices):
        MILLIGRAM = 1
        GRAM = 2
        MILLILITER = 3

    med_dose_unit = models.CharField(choices = Unit.choices,max_length=2)

    class Meta:
        ordering = ['med_date', 'med_time']

    def __str__(self):
        """String for representing the Model object."""
        return '{0} ({1})'.format(self.med_name, self.med_dose)

