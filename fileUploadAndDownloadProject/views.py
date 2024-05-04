from django.http import Http404, HttpResponse

from fileUploadAndDownloadProject.forms import UploadForm
from fileUploadAndDownloadProject.models import Files
from django.shortcuts import render, redirect


def home(request):
    files = Files.objects.all()
    return render(request, 'files/home.html', {'files': files})


# def home(request):
#  return render(request, 'files/home.html')


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


