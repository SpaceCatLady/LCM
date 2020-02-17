from django.shortcuts import render

# Create your views here.

from dlcm3.models import Medication, Unit, MedLog, MoodLog
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.core.exceptions import ValidationError
import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from django.urls import reverse
from dlcm3.forms import MedLogForm, MoodLogForm



def index(request):
    #View function for home page of site

    # Generate counts of some of the main objects
    num_meds = Medication.objects.all().count()
    num_entries = MedLog.objects.all().count()
    
    # number of visits  
    num_visits =  request.session.get('num_visits',0)
    request.session['num_visits'] = num_visits + 1
    
    context = {
        'num_meds': num_meds,
        'num_entries': num_entries,
        'num_visits' : num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class MedicationListView(LoginRequiredMixin, generic.ListView):
    model = Medication
    paginate_by = 10
    def get_queryset(self):
        return Medication.objects.filter(user_id=self.request.user)

class MedLogListView(LoginRequiredMixin, generic.ListView):
    model = MedLog
    paginate_by = 20
    def get_queryset(self):
        return MedLog.objects.filter(user_id=self.request.user)

class MedDetailView(LoginRequiredMixin,generic.DetailView):
    model = Medication
    paginate_by = 10

class MoodLogListView(LoginRequiredMixin,generic.ListView):
    model = MoodLog
    ordering = ('-mood_date')
    def get_queryset(self):
        return MoodLog.objects.filter(user_id=self.request.user).order_by('mood_date')

class MoodLogsListView(LoginRequiredMixin,generic.ListView):
    model = MoodLog
    def get_queryset(self):
        return MoodLog.objects.filter(user_id=self.request.user)

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class MedCreate(CreateView):
    model = Medication
    fields = ['name']
    def form_valid(self, form):
        form.instance.user_id = self.request.user
        return super().form_valid(form)


class MedUpdate(UpdateView):
    model = Medication
    fields = ['name']
    success_url = reverse_lazy('meds')

class MedDelete(DeleteView):
    model = Medication
    success_url = reverse_lazy('meds')

class MoodLogUpdate(UpdateView):
    model = MoodLog
    fields = ['mood_date', 'weight', 'sleep_hours', 'mood_score', 'bp_phase','life_event', 'life_event_effect', 'msw_count', 'other_symp','hosp_adm']
    success_url = reverse_lazy('mood-log')

class MoodLogDelete(DeleteView):
    model = MoodLog
    success_url = reverse_lazy('mood-log')

class MedLogUpdate(UpdateView):
    model = MedLog
    fields = ['med_time', 'med_id', 'med_dose', 'med_dose_unit', 'med_comment']
    #exclude = ['user']
    success_url = reverse_lazy('med-log')

class MedLogDelete(DeleteView):
    model = MedLog
    success_url = reverse_lazy('med-log')

class MoodLogDetailView(generic.DetailView):
    def get_queryset(self):
        return MoodLog.objects.filter(user_id=self.request.user)

class MedLogDetailView(generic.DetailView):
    def get_queryset(self):
        return MedLog.objects.filter(user_id=self.request.user)



#@permission_required('catalog.can_mark_returned')
def MedLogCreate(request):
    """View function for renewing a specific BookInstance by librarian."""
    #book_instance = get_object_or_404(BookInstance, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = MedLogForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            form.cleaned_data['user_id'] = request.user.id
            med_log = MedLog(**form.cleaned_data)
            med_log.save()
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('med-log'))

    # If this is a GET (or any other method) create the default form.
    else:
        #proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = MedLogForm()
        form.fields['med_id'].queryset = Medication.objects.filter(user_id=request.user) 

    context = {
        'form': form,
    }

    return render(request, 'dlcm3/med_log_create.html', context)

    #@permission_required('catalog.can_mark_returned')
from django.db import IntegrityError

def MoodLogCreate(request):
    """View function for renewing a specific BookInstance by librarian."""
    #book_instance = get_object_or_404(BookInstance, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = MoodLogForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            date = form.cleaned_data['mood_date']
            user_id = request.user.id
            count = MoodLog.objects.filter(mood_date = date).filter(user_id = user_id).count()
            print(f'number of entries{count}')
            if count > 0:
                #raise ValidationError(_('Invalid date - renewal in past'))
                form = MoodLogForm(request.POST)
                context = {
                    'form': form,
                    'duplicate': True
                 }   
                return render(request,'dlcm3/mood_log_create_duplicate.html', context)

                HttpResponse("form is duplicate here")
                print('why no error')
            form.cleaned_data['user_id'] = request.user.id
            mood_log = MoodLog(**form.cleaned_data)
            mood_log.save()
            return HttpResponseRedirect(reverse('mood-log'))
            

    # If this is a GET (or any other method) create the default form.
    else:
        #proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = MoodLogForm()
        #form.fields['med_id'].queryset = Medication.objects.filter(user_id=request.user) 

    context = {
        'form': form,
        'duplicate': False
    }

    return render(request, 'dlcm3/mood_log_create.html', context)