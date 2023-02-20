from django.contrib import admin
from .models import Calculation, Memory

# Register your models here.

admin.site.register(Calculation)
admin.site.register(Memory)