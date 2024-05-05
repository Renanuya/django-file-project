import os

from django.db import models


class Files(models.Model):
    """
    A Django model representing a file.

    Attributes:
        name (CharField): The name of the file.
        document (FileField): The file itself, stored as a FileField.
        uploaded_at (DateTimeField): The date and time the file was uploaded.
    """
    name = models.CharField(max_length=100)
    document = models.FileField(upload_to='files')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def delete(self, *args, **kwargs):
        """
       Overrides the default delete method to also delete the file from the filesystem.

       Args:
           *args: Variable length argument list.
           **kwargs: Arbitrary keyword arguments.
        """
        # Delete the file from the filesystem
        self.document.delete()
        # Call the default delete() implementation
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        """
        Overrides the default save method to update the file path in the database.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        # Update the file path in the database
        self.document.name = self.document.name
        super().save(*args, **kwargs)
