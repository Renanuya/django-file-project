from django.db import models


class Files(models.Model):
    name = models.CharField(max_length=100)
    document = models.FileField(upload_to='files')
    uploaded_at = models.DateTimeField(auto_now_add=True)