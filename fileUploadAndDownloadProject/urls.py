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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('files/<int:file_id>/', views.files, ),
    path('files/upload', views.upload, name='upload'),
    path('', views.home, name='home'),
    path('delete_file/<int:file_id>/', views.delete_file, name='delete_file'),
    path('rename_file/<int:file_id>/', views.rename_file, name='rename_file'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
