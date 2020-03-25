from django.contrib import admin
from .models import Work
from .models import Frase
from .models import Contact

# Register your models here.


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ['name','job', 'categories']
    search_fields = ['name','job']

@admin.register(Frase)
class FraseAdmin(admin.ModelAdmin):
    list_display = ['description']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']

