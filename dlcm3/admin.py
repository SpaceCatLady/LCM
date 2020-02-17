from django.contrib import admin
from .models import Medication, Unit, MedLog, MoodLog, Severity

# Register your models here.

class MedLogAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'med_time', 'med_id', 'med_dose', 'med_dose_unit', 'med_comment']
    list_filter = ['med_id']

    def med_name(self, obj):
        return obj.med_id.med_name
    def med_dose_unit_name(self, obj):
        return obj.med_dose_unit.med_dose_unit_name

admin.site.register(MedLog, MedLogAdmin)

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    pass

@admin.register(Medication)
class MedicationAdmin(admin.ModelAdmin):
    fields = ('name',)
    def save_model(self, request, obj, form, change):
        obj.name = request.user
        obj.save()
    pass

@admin.register(Severity)
class SeverityAdmin(admin.ModelAdmin):
    pass

class MoodLogAdmin(admin.ModelAdmin):
    list_display = ['mood_date' , 'bp_phase', 'other_symp', 'mood_score', 'msw_count', 'life_event', 'life_event_effect' , 'hosp_adm']

admin.site.register(MoodLog, MoodLogAdmin)