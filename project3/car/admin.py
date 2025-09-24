from django.contrib import admin
from .models import Car
# Register your models here.

admin.site.register(Car)

class CarAdmin(admin.ModelAdmin):
    list_display = ('id','brand','model','year','price','type')
    search_fields = ("brand", "model", "type")  
    list_filter = ("year", "type")              
    ordering = ("id",)