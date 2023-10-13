from django.contrib import admin
from .models import destination

# Register your models here.
@admin.register(destination)
class destination1(admin.ModelAdmin):
    list_display = ['id','price','img','name','offer']