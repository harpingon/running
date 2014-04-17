from django.contrib import admin

# Register your models here.
from .models import Run, Manufacturer, Shoe

class ManufacturerAdmin(admin.ModelAdmin):
    fields = ("name",)
    list_display = ["name",]
#    list_display_links = ["name",]
#    list_editable = ["name",]
#    list_filter = ["name",]
    search_fileds = ["name",]

class ShoeAdmin(admin.ModelAdmin):
    fields = ("user","name","purchased","rating","manufacturer",)
    list_display = ["user","name","purchased","rating","manufacturer",]
    list_editable = ["purchased","rating","manufacturer",]
    list_filter = ["manufacturer",]
    search_fields = ["name","manufacturer",]

class RunAdmin(admin.ModelAdmin):
    fields = ("user","rundate","distance","calories","shoe","notes",)
    list_display = ["user","rundate","distance","calories","shoe","notes",]
    list_editable = ["distance","calories","shoe","notes",]
    list_filter = ["shoe",]

admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Shoe, ShoeAdmin)
admin.site.register(Run, RunAdmin)
