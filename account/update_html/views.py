from django.shortcuts import render
from .forms import UploadFileForm
from .models import MyData
import io
import os
from io import StringIO
import csv
from django.template.loader import render_to_string
from django.contrib import messages

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['file']
            print(csv_file)
            decoded_file = csv_file.read().decode('utf-8')
            print(decoded_file)
            io_string = io.StringIO(decoded_file)
            print(io_string)
            reader = csv.reader(io_string)
            print(reader)

            for row in reader:
                _, created = MyData.objects.get_or_create(
                    file_name=row[0],
                    title=row[1],
                    image_link=row[2],
                    url_link=row[3],
                    sambol=row[4]
                    # Add more fields as needed
                )
                directory_path='E:/Account'
                os.makedirs(directory_path, exist_ok=True)
                template_data = {'file_name':row[0],'title':row[1],'image_link':row[2],'url_link':row[3],'sambol':row[4]}
                html_content = render_to_string('video-.espn10.html', template_data)
                #Save The Html Content in Html
                file_path = os.path.join(directory_path, f'{row[0]}.html')
                print(file_path)
                with open(file_path,'w', encoding='utf-8') as html_file:
                    html_file.write(html_content)
                    messages.success(request,"File Upload Done and Html file Created Done Kindly check your Dir")

    else:
        form = UploadFileForm()

    return render(request, 'upload_file.html', {'form': form})
