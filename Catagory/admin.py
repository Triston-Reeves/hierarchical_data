from django.contrib import admin
from Catagory.models import Catagory
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin

# Register your models here.

admin.site.register(Catagory, DraggableMPTTAdmin)