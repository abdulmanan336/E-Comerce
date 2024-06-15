from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Contact)


admin.site.site_header = "New Clean Wash"
admin.site.site_title = "New Clean Wash"
admin.site.index_title  = "New Clean Wash"