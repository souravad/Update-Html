from django.db import models

class MyData(models.Model):
    file_name = models.CharField(max_length=5000)
    title = models.CharField(max_length=5000)
    image_link = models.CharField(max_length=5000)
    url_link = models.CharField(max_length=5000)
    sambol = models.CharField(max_length=5000)
    # Add more fields as needed
