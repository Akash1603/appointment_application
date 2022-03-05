from django.urls import path

from app_service.views import AppointmentListView, AppointmentCreateView, AppointmentDetailView, AppointmentUpdateView, \
    AppointmentDeleteView

urlpatterns = [
    path('new/', AppointmentCreateView.as_view(), name='new_appointment'),
    path("alist/", AppointmentListView.as_view(), name='alist'),
    path('vlist/<int:pk>', AppointmentDetailView.as_view(), name='vlist'),
    path('ulist/<int:pk>', AppointmentUpdateView.as_view(), name='ulist'),
    path('dlist/<int:pk>', AppointmentDeleteView.as_view(), name='dlist'),
]
