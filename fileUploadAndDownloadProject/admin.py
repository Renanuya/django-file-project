from django.contrib import admin
from .models import Files


class FilesAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(Files, FilesAdmin)
