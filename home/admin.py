from django.contrib import admin
from . models import Profile,Doctor,Patient,Record
# Register your models here.
admin.site.register(Profile)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Record)