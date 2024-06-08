from django.contrib import admin

# Register your models here.
from .models import Concert

# asi se registra un modelo en django
admin.site.register(Concert)