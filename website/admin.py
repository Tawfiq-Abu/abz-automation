from django.contrib import admin
from .models import TeamMember

from .models import Metric

# Register your models here.
admin.site.register(TeamMember)
# class TeamMemberAdmin(admin.ModelAdmin):
#     list_display= ['firstname','othername', 'lastname','role','image','linked_in','email']


admin.site.register(Metric)
