from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    image = models.ImageField(upload_to='image/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    date_of_birth = models.DateField()


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    speciality = models.CharField(max_length=32)
    license_number = models.PositiveIntegerField(default=0)
    years_of_experience = models.SmallIntegerField(default=0)
    education = models.CharField(max_length=60)
    hospital = models.CharField(max_length=60)


class MedicalRecord(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    record_type = models.CharField(max_length=32)
    description = models.TextField()
    date = models.DateTimeField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)


class Appointment(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    reason = models.TextField()


class Medication(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()


class FitnessProgram(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()


class Notification(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)






