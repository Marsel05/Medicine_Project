from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class UserProfileViewSets(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class DoctorViewSets(ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['education', 'hospital', 'speciality']
    search_fields = ["license_number"]

class MedicalRecordViewSets(ModelViewSet):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializers


class AppointmentViewSets(ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializers


class MedicationViewSets(ModelViewSet):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializers


class FitnessProgramViewSets(ModelViewSet):
    queryset = FitnessProgram.objects.all()
    serializer_class = FitnessProgramSerializers


class NotificationViewSets(ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]