from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin


admin.site.register(UserProfile)
admin.site.register(MedicalRecord)
admin.site.register(Appointment)
admin.site.register(Medication)
admin.site.register(FitnessProgram)
admin.site.register(Notification)


@admin.register(Doctor)
class DoctorAdmin(TranslationAdmin):
    list_display = ('speciality', 'education', 'hospital')

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
