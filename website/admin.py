from django.contrib import admin
from .models import TeamMember

from .models import Metric,Feature,Product,Service

# Register your models here.
admin.site.register(TeamMember)
# class TeamMemberAdmin(admin.ModelAdmin):
#     list_display= ['firstname','othername', 'lastname','role','image','linked_in','email']


admin.site.register(Metric)
admin.site.register(Product)
admin.site.register(Feature)
admin.site.register(Service)



