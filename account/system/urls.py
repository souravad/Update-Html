# urls.py
from django.urls import path
from .views import generate_and_download_html,addinforma,get_latest_product



urlpatterns = [
    path('addinforma/', addinforma, name='addinforma'),
    path('generate-and-download/', generate_and_download_html, name='generate-and-download'),
    path('get_latest_product/', get_latest_product, name='get_latest_product')
    # Other URL patterns
]
