"""CoverLetterGenerator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
import coverLetters.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', coverLetters.views.homepage, name='homepage'),
    path('all-jobs', coverLetters.views.all_jobs, name='all-jobs')
    path('job-detail/<int:job_id>', coverLetters.views.detail, name='job-detail'),
    path('cover-letter', coverLetters.views.detail, name='cover-letter-form')
]
