import os

from django.db import models


class Files(models.Model):
    name = models.CharField(max_length=100)
    document = models.FileField(upload_to='files')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def delete(self, *args, **kwargs):
        # Delete the file from the filesystem
        self.document.delete()
        # Call the default delete() implementation
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        # Update the file path in the database
        self.document.name = self.document.name
        super().save(*args, **kwargs)