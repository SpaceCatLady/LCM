from django.urls import path

from . import views
from .models import MedicineLog

urlpatterns = [
    path('', views.index, name='index'),
 	path('meds/create/', views.SectionMedCreate.as_view(), name='meds_create'),
    path('meds/', views.MedListView.as_view(), name='meds'),
 	    ]