from core.admin import Yearupdate
from core.models import Faculty,Yearupdate
from django.contrib.auth.decorators import login_required
from django_filters.rest_framework import DjangoFilterBackend
from faculty.filters import UserFilter
from rest_framework import generics, authentication, permissions
from faculty.serializers import FacultySerializer, YearSerializer
from django.http import JsonResponse
from django.shortcuts import render  
from faculty.forms import FacultyForm, FacultyUpdateForm
import pandas as pd
import numpy as np
import json
from django.db.models import Max,Min
import decimal



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
        return np.nan
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
                        CAY_FAP_Score = check(row[11]),
                        CAY_Feedback_Score = check(row[12]),
                        CAY_FRP_Score = check(row[13]),
                        CAY_FRS = check(row[14]),
                        CAYM1_FAP_Score = check(row[15]),
                        CAYM1_Feedback_Score = check(row[16]),
                        CAYM1_FRP_Score = check(row[17]),
                        CAYM1_FRS= check(row[18]),
                        CAYM2_FAP_Score = check(row[19]),
                        CAYM2_Feedback_Score = check(row[20]),
                        CAYM2_FRP_Score= check(row[21]),
                        CAYM2_FRS = check(row[22]),
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
                    elif field == 'CAY_FAP_Score':
                        Faculty.objects.filter(faculty_id=df[faculty_id]).update(CAY_FAP_Score=check(df[field_name]))
                    elif field == 'CAY_Feedback_Score':
                        Faculty.objects.filter(faculty_id=df[faculty_id]).update(CAY_Feedback_Score=check(df[field_name]))
                    elif field == 'CAY_FRP_Score':
                        Faculty.objects.filter(faculty_id=df[faculty_id]).update(CAY_FRP_Score=check(df[field_name]))
                    elif field == 'CAY_FRS':
                        Faculty.objects.filter(faculty_id=df[faculty_id]).update(CAY_FRS=check(df[field_name]))
                    elif field == 'CAYM1_FAP_Score':
                        Faculty.objects.filter(faculty_id=df[faculty_id]).update(CAYM1_FAP_Score=check(df[field_name]))
                    elif field == 'CAYM1_Feedback_Score':
                        Faculty.objects.filter(faculty_id=df[faculty_id]).update(CAYM1_Feedback_Score=check(df[field_name]))
                    elif field == 'CAYM1_FRP_Score':
                        Faculty.objects.filter(faculty_id=df[faculty_id]).update(CAYM1_FRP_Score=check(df[field_name]))
                    elif field == 'CAYM1_FRS':
                        Faculty.objects.filter(faculty_id=df[faculty_id]).update(CAYM1_FRS=check(df[field_name]))
                    elif field == 'CAYM2_FAP_Score':
                        Faculty.objects.filter(faculty_id=df[faculty_id]).update(CAYM2_FAP_Score=check(df[field_name]))
                    elif field == 'CAYM2_Feedback_Score':
                        Faculty.objects.filter(faculty_id=df[faculty_id]).update(CAYM2_Feedback_Score=check(df[field_name]))
                    elif field == 'CAYM2_FRP_Score':
                        Faculty.objects.filter(faculty_id=df[faculty_id]).update(CAYM2_FRP_Score=check(df[field_name]))
                    elif field == 'CAYM2_FRS':
                        Faculty.objects.filter(faculty_id=df[faculty_id]).update(CAYM2_FRS=check(df[field_name]))
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

def minmax(request):  
    """View for updating existing data from the file"""
    FAP_MIN = Faculty.objects.all().filter(CAY_FAP_Score__isnull=False).exclude(CAY_FAP_Score='NaN').aggregate(Min('CAY_FAP_Score'))
    FAP_MAX = Faculty.objects.all().filter(CAY_FAP_Score__isnull=False).exclude(CAY_FAP_Score='NaN').aggregate(Max('CAY_FAP_Score'))
    FEEDBACK_MIN = Faculty.objects.all().filter(CAY_Feedback_Score__isnull=False).exclude(CAY_Feedback_Score='NaN').aggregate(Min('CAY_Feedback_Score'))
    FEEDBACK_MAX = Faculty.objects.all().filter(CAY_Feedback_Score__isnull=False).exclude(CAY_Feedback_Score='NaN').aggregate(Max('CAY_Feedback_Score'))
    FRP_MIN = Faculty.objects.all().filter(CAY_FRP_Score__isnull=False).exclude(CAY_FRP_Score='NaN').aggregate(Min('CAY_FRP_Score'))
    FRP_MAX = Faculty.objects.all().filter(CAY_FRP_Score__isnull=False).exclude(CAY_FRP_Score='NaN').aggregate(Max('CAY_FRP_Score'))
    FRS_MIN = Faculty.objects.all().filter(CAY_FRS__isnull=False).exclude(CAY_FRS='NaN').aggregate(Min('CAY_FRS'))
    FRS_MAX = Faculty.objects.all().filter(CAY_FRS__isnull=False).exclude(CAY_FRS='NaN').aggregate(Max('CAY_FRS'))   
        
    data=[FAP_MIN,FAP_MAX,
            FEEDBACK_MIN,FEEDBACK_MAX,
            FRP_MIN,FRP_MAX,
            FRS_MIN,FRS_MAX,
    ]
    return JsonResponse(data, safe=False)
 

class AcademicYearView(generics.ListAPIView):
    """API view for Academic years"""
    queryset = Yearupdate.objects.all()
    serializer_class = YearSerializer
    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAuthenticated,)
    # filter_backends = [DjangoFilterBackend,]
    # filterset_class = UserFilter
    # filterset_fields = ['faculty_id', 'name', 'designation', 'department', 'central_responsibility', 'status', 'date_of_joining', 'mobile_number', 'email' ]
