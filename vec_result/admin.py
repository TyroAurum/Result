from django.contrib import admin
from .models import PinkIT
from import_export.admin import ImportExportModelAdmin
# Register your models here.


@admin.register(PinkIT)
class ResultsData(ImportExportModelAdmin):
    pass
