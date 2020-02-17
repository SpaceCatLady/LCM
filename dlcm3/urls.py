from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name = 'index'),
	path('meds/', views.MedicationListView.as_view(), name = 'meds'),
	path('medlog/', views.MedLogListView.as_view(), name = 'med-log'),
	path('moodlog/', views.MoodLogListView.as_view(), name = 'mood-log'),
	path('meds/<int:pk>', views.MedDetailView.as_view(), name = 'med-detail'),
	path('meds/create/', views.MedCreate.as_view(), name='meds-create'),
	path('meds/<int:pk>/update/', views.MedUpdate.as_view(), name='meds-update'),
    path('meds/<int:pk>/delete/', views.MedDelete.as_view(), name='meds-delete'),
    path('moodlog/<int:pk>', views.MoodLogDetailView.as_view(), name = 'mood-log-detail'),
    path('moodlog/create/', views.MoodLogCreate, name='mood-log-create'),
    path('moodlog/<int:pk>/update/', views.MoodLogUpdate.as_view(), name='mood-log-update'),
    path('moodlog/<int:pk>/delete/', views.MoodLogDelete.as_view(), name='mood-log-delete'),
    path('medlog/<int:pk>', views.MedLogDetailView.as_view(), name = 'med-log-detail'),
    path('medlog/<int:pk>/update/', views.MedLogUpdate.as_view(), name='med-log-update'),
    path('medlog/<int:pk>/delete/', views.MedLogDelete.as_view(), name='med-log-delete'),
    path('medlog/create/', views.MedLogCreate, name='med-log-create'),
    ]

