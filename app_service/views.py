from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from app_service.form import CustomerForm
from app_service.models import Appointment


class AppointmentCreateView(SuccessMessageMixin, CreateView):
    model = Appointment
    form_class = CustomerForm
    success_url = reverse_lazy('alist')
    template_name = 'app_service/appointment_form.html'
    success_message = 'Appointment successfully created!.'


class AppointmentListView(ListView):
    model = Appointment
    template_name = 'app_service/appointment_list.html'
    context_object_name = 'apps'
    paginate_by = 4

    def get_queryset(self):
        return Appointment.objects.order_by('-id')


class AppointmentDetailView(DetailView):
    model = Appointment
    template_name = 'app_service/appointment_detail.html'


class AppointmentUpdateView(UpdateView):
    model = Appointment
    template_name = 'app_service/appointment_update.html'
    form_class = CustomerForm
    success_message = 'Success: Data was updated.'
    success_url = reverse_lazy('alist')


class AppointmentDeleteView(DeleteView):
    model = Appointment
    template_name = 'app_service/confirm_delete.html'
    success_url = reverse_lazy('alist')
