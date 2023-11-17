# views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.conf import settings
import os
import io
from .models import Product
from .forms import GenerateHTMLForm

def addinforma(request):
    form=GenerateHTMLForm()
    if request.method=='POST':
        form=GenerateHTMLForm(request.POST)
        if form.is_valid():
            form.save()
    return render (request,'base.html', context={'form':form})

def generate_and_download_html(request):
    products = Product.objects.latest('created_at')  # Fetch all products (apply filters as needed)
    product_title=products.title
    product_image=products.image
    product_url=products.url
    rendered_html = render_to_string('video-.espn10.html', {'product_title': product_title,'product_image':product_image,'product_url':product_url})

    # Define the file path and name
    file_path = os.path.join(settings.MEDIA_ROOT, 'vedio.html')

    # Write content to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(rendered_html)

    # Serve the file for download
    with open(file_path, 'r', encoding='utf-8') as file:
        response = HttpResponse(file, content_type='text/html')
        response['Content-Disposition'] = 'attachment; filename="vedio.html"'
        return response


def get_latest_product(request):
    latest_product = Product.objects.latest('created_at')
    product_name = latest_product.title  # Access the property directly
    print('Title : ', product_name)
    # Perform operations with the latest product data
    return HttpResponse(f"The latest product is: {product_name}")