from django.contrib import admin
from .models import Personnel

@admin.register(Personnel)
class PersonnelAdmin(admin.ModelAdmin):
  list_display = ('full_name','rank_position', 'unit_section', 'contact_number')
  search_fields = ('full_name', 'rank_position', 'unit_position')

