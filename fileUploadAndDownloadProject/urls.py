"""
URL configuration for fileUploadProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from fileUploadAndDownloadProject import views
from django.conf import settings

# Define the URL patterns for the application
urlpatterns = [

    # URL pattern for the admin site
    path('admin/', admin.site.urls),

    # URL pattern for accessing a specific file
    # The file_id is passed as a parameter in the URL
    path('files/<int:file_id>/', views.files, ),

    # URL pattern for uploading a file
    path('files/upload', views.upload, name='upload'),

    # URL pattern for the home page
    path('', views.home, name='home'),

    # URL pattern for deleting a specific file
    # The file_id is passed as a parameter in the URL
    path('delete_file/<int:file_id>/', views.delete_file, name='delete_file'),

    # URL pattern for renaming a specific file
    # The file_id is passed as a parameter in the URL
    path('rename_file/<int:file_id>/', views.rename_file, name='rename_file'),
]

# Add the media URL and document root to the URL patterns
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
