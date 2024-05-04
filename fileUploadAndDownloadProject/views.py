import os

from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.urls import reverse

from fileUploadAndDownloadProject import settings
from fileUploadAndDownloadProject.forms import UploadForm
from fileUploadAndDownloadProject.models import Files
from django.shortcuts import render, redirect


def home(request):
    files = Files.objects.all()
    return render(request, 'files/home.html', {'files': files})


def files(request, file_id):
    file = Files.objects.get(pk=file_id)


def upload(request):
    if request.POST:
        form = UploadForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            form.save()
        return redirect(home)
    return render(request, 'files/upload.html', {'form': UploadForm})


def delete_file(request, file_id):
    file = Files.objects.get(pk=file_id)
    file_path = os.path.join(settings.MEDIA_ROOT, file.document.name)
    if os.path.exists(file_path):
        os.remove(file_path)
    file.delete()
    return redirect('home')
