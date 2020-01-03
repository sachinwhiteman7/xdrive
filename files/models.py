from django.db import models


class FileUpload(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    file = models.FileField(upload_to='file')
    file_name = models.CharField(max_length=1024)
    file_type = models.CharField(max_length=64)
