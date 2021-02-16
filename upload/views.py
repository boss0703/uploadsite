from django.shortcuts import render, redirect
from django.utils import timezone

from upload.forms import UploadForm
from upload.models import ImageFileModel


def index(request):
    if request.method == 'POST':
        print("-- post --")
        form = UploadForm(request.POST or None)
        if form.is_valid():
            print("valid")
            image_file = ImageFileModel()
            image_file.image = request.FILES['image']
            image_file.published_date = timezone.now()

            image_file.save()
            form.save()
            render(request, 'upload/index.html', {'form': form})
        else:
            print("not")
            form = UploadForm()
            render(request, 'upload/index.html', {'form': form})
    else:
        form = UploadForm()
    return render(request, 'upload/index.html', {'form': form})


