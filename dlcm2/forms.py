from django.forms import ModelForm
from .models import sectionMed


class formMed(ModelForm):
    def clean_med_form(self):
       data = self.cleaned_data['med_time', 'med_name', 'med_dose', 'med_dose_unit']
       
       # Check if a date is not in the past.
       if data > datetime.date.today():
           raise ValidationError(_('Invalid date - medicine intake in future'))

       # Remember to always return the cleaned data.
       return data

    class Meta:
        model = sectionMed
        fields = ['med_time', 'med_name', 'med_dose', 'med_dose_unit']
        labels = {'med_time':  ('Time medicine taken'),
        			'med_name':  ('Name of medicine'),
        			'med_dose':  ('Dosage of medicine taken'),
        			'med_dose_unit':  ('Dosage units')
        			}
        help_texts = {'med_time':  ('Select time'),
        			'med_name':  ('Enter medicine name'),
        			'med_dose':  ('Enter dosage taken'),
        			'med_dose_unit':  ('Select dosage units')
        			}