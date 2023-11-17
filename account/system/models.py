# models.py
from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=1000,blank=False)
    image = models.CharField(max_length=1000,blank=False)
    url = models.CharField(max_length=1000,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        get_latest_by = 'created_at'
    # Add more fields as needed
