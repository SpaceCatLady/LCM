from django.shortcuts import render
from django.http import HttpResponse
from .models import MedicineLog
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the daily life chart method index.")

class MedListView(generic.ListView):
    """Generic class-based view for a list of medicine intake."""
    model = MedicineLog
    paginate_by = 10

class SectionMedCreate(CreateView):
    model = MedicineLog
    fields = '__all__'