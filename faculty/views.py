from core.models import Faculty
from django.contrib.auth.decorators import login_required
from django_filters.rest_framework import DjangoFilterBackend
from faculty.filters import UserFilter
from rest_framework import generics, authentication, permissions
from faculty.serializers import FacultySerializer
from django.http import JsonResponse
from django.shortcuts import render  
from faculty.forms import FacultyForm, FacultyUpdateForm
import pandas as pd
import numpy as np
import json
        
class FacultyListView(generics.ListAPIView):
    """API view for faculty lists"""
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [DjangoFilterBackend,]
    filterset_class = UserFilter
    # filterset_fields = ['faculty_id', 'name', 'designation', 'department', 'central_responsibility', 'status', 'date_of_joining', 'mobile_number', 'email' ]


def check(a):
    if pd.isnull(a):
        return np.nan_to_num(a)
    else:
        if isinstance(a, int):
            return a
        elif isinstance(a, float):
            return a
        else:
            return None

def file_upload(request):
    """View for adding new data from the file"""
    if request.user.is_authenticated:  
        if request.method == 'POST': 
            form = FacultyForm(request.POST, request.FILES)
            if form.is_valid():
                upload = request.FILES['file']
                df = pd.read_excel(upload)
                df = df[1: : ]
                row_iter = df.iterrows()

                
                objs = [
                    Faculty(
                        faculty_id = row[1],
                        name  = row[2],
                        designation  = row[3],
                        department  = row[4],
                        central_responsibility = row[5],
                        status = row[6],
                        date_of_joining = pd.to_datetime(row[7]).strftime('%Y-%m-%d'),
                        mobile_number = row[8],
                        email = row[9],
                        picture = row[10],
                        FAP_1920_Score = check(row[11]),
                        Feedback_1920_Score = check(row[12]),
                        FRP_1920 = check(row[13]),
                        FRS_1920 = check(row[14]),
                        FAP_2021_Score = check(row[15]),
                        Feedback_2021_Score = check(row[16]),
                        FRP_2021 = check(row[17]),
                        FRS_2021 = check(row[18]),
                        FAP_2122_Score = check(row[19]),
                        Feedback_2122_Score = check(row[20]),
                        FRP_2122 = check(row[21]),
                        FRS_2122 = check(row[22]),
                        Faculty_list = row[23],
                        About = row[24],
                        Search = row[25]
                        )
                    for index, row in row_iter
                    ]
                Faculty.objects.bulk_create(objs)
                return render(request, "upload_msg.html")

        else:  
            faculty = FacultyForm()  
            return render(request,"upload.html",{'form':faculty}) 
    
    else:
        return render(request, "login_required.html")

def file_update(request):  
    """View for updating existing data from the file"""
    if request.user.is_authenticated:
        if request.method == 'POST': 
            form = FacultyUpdateForm(request.POST, request.FILES)
            if form.is_valid():
                upload = request.FILES['file']
                df = pd.read_excel(upload)
                js = df.to_json(orient='records')
                js = json.loads(js)
                faculty_id = form.cleaned_data['Faculty_Id']
                field = form.cleaned_data['field']
                field_name = form.cleaned_data['field_name']
                for df in js:
                    if field == 'name':
                        Faculty.objects.filter(faculty_id=df[faculty_id]).update(name=df[field_name])
                    elif field == 'designation':
                        Faculty.objects.filter(faculty_id=df[faculty_id]).update(designation=df[field_name])
                    elif field == 'department':
                        Faculty.objects.filter(faculty_id=df[faculty_id]).update(departmentname=df[field_name])
                    elif field == 'central_responsibility':
                        Faculty.objects.filter(faculty_id=df[faculty_id]).update(central_responsibility=df[field_name])
                    elif field == 'status':
                        Faculty.objects.filter(faculty_id=df[faculty_id]).update(status=df[field_name])
                    elif field == 'date_of_joining':
                        Faculty.objects.filter(faculty_id=df[faculty_id]).update(date_of_joining=df[field_name])
                    elif field == 'mobile_number':
                        Faculty.objects.filter(faculty_id=df[faculty_id]).update(mobile_number=df[field_name])
                    elif field == 'picture':
                        Faculty.objects.filter(faculty_id=df[faculty_id]).update(picture=df[field_name])
                    elif field == 'FAP_1920_Score':
                        Faculty.objects.filter(faculty_id=df[faculty_id]).update(FAP_1920_Score=check(df[field_name]))
                    elif field == 'Feedback_1920_Score':
                        Faculty.objects.filter(faculty_id=df[faculty_id]).update(Feedback_1920_Score=check(df[field_name]))
                    elif field == 'FRP_1920':
                        Faculty.objects.filter(faculty_id=df[faculty_id]).update(FRP_1920=check(df[field_name]))
                    elif field == 'FRS_1920':
                        Faculty.objects.filter(faculty_id=df[faculty_id]).update(FRS_1920=check(df[field_name]))
                    elif field == 'FAP_2021_Score':
                        Faculty.objects.filter(faculty_id=df[faculty_id]).update(FAP_2021_Score=check(df[field_name]))
                    elif field == 'Feedback_2021_Score':
                        Faculty.objects.filter(faculty_id=df[faculty_id]).update(Feedback_2021_Score=check(df[field_name]))
                    elif field == 'FRP_2021':
                        Faculty.objects.filter(faculty_id=df[faculty_id]).update(FRP_2021=check(df[field_name]))
                    elif field == 'FRS_2021':
                        Faculty.objects.filter(faculty_id=df[faculty_id]).update(FRS_2021=check(df[field_name]))
                    elif field == 'FAP_2122_Score':
                        Faculty.objects.filter(faculty_id=df[faculty_id]).update(FAP_2122_Score=check(df[field_name]))
                    elif field == 'Feedback_2122':
                        Faculty.objects.filter(faculty_id=df[faculty_id]).update(Feedback_2122=check(df[field_name]))
                    elif field == 'FRP_2122':
                        Faculty.objects.filter(faculty_id=df[faculty_id]).update(FRP_2122=check(df[field_name]))
                    elif field == 'FRS_2122':
                        Faculty.objects.filter(faculty_id=df[faculty_id]).update(FRS_2122=check(df[field_name]))
                    elif field == 'Faculty_List':
                        Faculty.objects.filter(faculty_id=df[faculty_id]).update(Faculty_list=df[field_name])
                    elif field == 'About':
                        Faculty.objects.filter(faculty_id=df[faculty_id]).update(About=df[field_name])
                    elif field == 'Search':
                        Faculty.objects.filter(faculty_id=df[faculty_id]).update(Search=df[field_name])
    
                return render(request, "update_msg.html")
                
        else:  
            faculty_update = FacultyUpdateForm() 
            return render(request, "update.html", {'form':faculty_update})

    else:
        return render(request, "login_required.html")
 
    
 
    

def dept(request):
    """API view for department list"""
    data = list(Faculty.objects.values_list('department', flat=True).distinct().order_by('department')) # wrap in list(), because QuerySet is not JSON serializable
    return JsonResponse(data, safe=False)

def designation(request):
    """API view for designation list"""
    data = list(Faculty.objects.values_list('designation', flat=True).distinct().order_by('designation'))
    return JsonResponse(data, safe=False)

def cen_res(request):
    """API view for central responsibility list"""
    data = list(Faculty.objects.values_list('central_responsibility', flat=True).distinct().order_by('central_responsibility')) # wrap in list(), because QuerySet is not JSON serializable
    return JsonResponse(data, safe=False)

def status(request):
    """API view for status list"""
    data = list(Faculty.objects.values_list('status', flat=True).distinct().order_by('status')) # wrap in list(), because QuerySet is not JSON serializable
    return JsonResponse(data, safe=False)
