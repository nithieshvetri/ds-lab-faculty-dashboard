import django_filters

from core.models import Faculty

class UserFilter(django_filters.FilterSet):
    """Filters for Faculty model"""
    class Meta:
        model = Faculty
        fields = {
            'faculty_id': ['icontains'],
            'name': ['icontains',],
            "designation": ['icontains',],
            "department": ['icontains',],
            "central_responsibility": ['icontains',],
            "status": ['icontains',],
            "date_of_joining": ['exact', 'year__gte',],
            "mobile_number": ['icontains',],
            "email": ['icontains',],
            "FAP_1920_Score":['lte', 'gte'],
            'Feedback_1920_Score':['lte', 'gte'],
            "FRP_1920":['lte', 'gte'],
            'FRS_1920':['lte', 'gte'],
            "FAP_2021_Score":['lte', 'gte'],
            'Feedback_2021_Score':['lte', 'gte'],
            "FRP_2021":['lte', 'gte'],
            'FRS_2021':['lte', 'gte'],
            "FAP_2122_Score":['lte', 'gte'],
            'Feedback_2122_Score':['lte', 'gte'],
            "FRP_2122":['lte', 'gte'],
            'FRS_2122':['lte', 'gte'],
            "About": ['icontains',],
        }