from .views import *
from django.urls.conf import path

urlpatterns = [
    path('user/', UserProfileViewSets.as_view({'get': 'list', 'post': 'create'}
                                  ), name="userprofile_list"),
    path("user/<int:pk>/", UserProfileViewSets.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}
                                          ), name="userprofile_detail"),

    path('doctor/', DoctorViewSets.as_view({'get': "list", "post": "create"}
                                   ),name="doctor_list"),
    path("doctor/<int:pk>/", DoctorViewSets.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}
                                     ),name="doctor_detail"),

    path('record/', MedicalRecordViewSets.as_view({'get': "list", "post": "create"}
                                          ),name="medical_record_list"),
    path("record/<int:pk>/", MedicalRecordViewSets.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}
                                            ),name="medical_record_detail"),
    path('appointment/', AppointmentViewSets.as_view({'get': "list", "post": "create"}
                                             ),name="appointment_list"),
    path("appointment/<int:pk>/", AppointmentViewSets.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}
                                          ),name="appointment_detail"),
    path('medication/', MedicationViewSets.as_view({'get': "list", "post": "create"}
                                           ),name="medication_list"),
    path("medication/<int:pk>/", MedicationViewSets.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}
                                         ),name="medication_detail"),
    path('fitness/', FitnessProgramViewSets.as_view({'get': "list", "post": "create"}
                                            ),name="fitness_program_list"),
    path("fitness/<int:pk>/", FitnessProgramViewSets.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}
                                             ),name="fitness_program_detail"),
    path('notification/', NotificationViewSets.as_view({'get': "list", "post": "create"}
                                               ),name="notification_list"),
    path("notification/<int:pk>/", NotificationViewSets.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}
                                           ),name="notification_detail"),
]
