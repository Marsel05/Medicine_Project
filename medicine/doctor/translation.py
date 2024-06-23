from .models import Doctor
from modeltranslation.translator import TranslationOptions, register


@register(Doctor)
class DoctorTranslationOptions(TranslationOptions):
    fields = ('speciality', 'education', 'hospital')