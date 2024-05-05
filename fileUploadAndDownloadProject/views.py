import os
from fileUploadAndDownloadProject import settings
from fileUploadAndDownloadProject.forms import UploadForm, RenameFileForm
from fileUploadAndDownloadProject.models import Files
from django.shortcuts import render, redirect


# Home view function
def home(request):
    """
    This function handles the home view. It retrieves all files from the database and renders them on the home page.
    """
    files = Files.objects.all()
    return render(request, 'files/home.html', {'files': files})


# File view function
def files(request, file_id):
    """
    This function handles the file view. It retrieves a specific file from the database using its id.
    """
    file = Files.objects.get(pk=file_id)


# Upload view function
def upload(request):
    """
    This function handles the file upload view. It validates and saves the uploaded file if the request method is POST.
    Otherwise, it renders the upload form.
    """
    if request.POST:
        form = UploadForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            form.save()
        return redirect(home)
    return render(request, 'files/upload.html', {'form': UploadForm})


# Delete file view function
def delete_file(request, file_id):
    """
    This function handles the file deletion view. It deletes a specific file from the database and the file system
    using its id.
    """
    file = Files.objects.get(pk=file_id)
    file_path = os.path.join(settings.MEDIA_ROOT, file.document.name)
    if os.path.exists(file_path):
        os.remove(file_path)
    file.delete()
    return redirect('home')


# Rename file view function
def rename_file(request, file_id):
    """
    This function handles the file renaming view. It renames a specific file in the database and the file system
    using its id.
    """
    file = Files.objects.get(pk=file_id)
    if request.method == 'POST':
        form = RenameFileForm(request.POST)
        if form.is_valid():
            new_name = form.cleaned_data['new_name']
            # Get the file extension
            _, ext = os.path.splitext(file.document.name)
            # Update the file name
            file.name = new_name
            # Update the file path in the database
            new_file_path = os.path.join('files', new_name + ext)
            old_file_path = file.document.path
            file.document.name = new_file_path
            # Rename the actual file
            os.rename(old_file_path, os.path.join(settings.MEDIA_ROOT, new_file_path))
            file.save()
            return redirect('home')
    else:
        form = RenameFileForm()
    return render(request, 'files/rename.html', {'file': file, 'form': form})
