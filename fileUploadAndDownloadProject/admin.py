from django.contrib import admin
from .models import Files


# Define a new admin interface for the Files model
class FilesAdmin(admin.ModelAdmin):
    # Specify the fields that are read-only in the admin interface
    readonly_fields = ('id',)


# Register the Files model and its admin interface with the Django admin site
admin.site.register(Files, FilesAdmin)
