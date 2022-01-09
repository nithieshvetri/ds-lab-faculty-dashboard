from django.http import request
from django.urls import path

from faculty import views


app_name = 'faculty'

urlpatterns = [
    path('lists/', views.FacultyListView.as_view()), # listing all faculty data
    path('dept/', views.dept,), # listing all department
    path('designation/', views.designation,), # listing all designation
    path('cr/', views.cen_res,), # listing central responsibility
    path('status/', views.status,), # listing status
    path('minmax/', views.minmax,), # api for slider minimum & maximum
    path('upload/', views.file_upload), # uploading file for uploading new data 
    path('fileupdate/', views.file_update), # upload file for updating existing data
    path('academic/',views.AcademicYearView.as_view())

]
