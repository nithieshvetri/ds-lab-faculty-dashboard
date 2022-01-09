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
            "CAY_FAP_Score":['lte', 'gte'],
            'CAY_Feedback_Score':['lte', 'gte'],
            "CAY_FRP_Score":['lte', 'gte'],
            'CAY_FRS':['lte', 'gte'],
            "CAYM1_FAP_Score":['lte', 'gte'],
            'CAYM1_Feedback_Score':['lte', 'gte'],
            "CAYM1_FRP_Score":['lte', 'gte'],
            'CAYM1_FRS':['lte', 'gte'],
            "CAYM2_FAP_Score":['lte', 'gte'],
            'CAYM2_Feedback_Score':['lte', 'gte'],
            "CAYM2_FRP_Score":['lte', 'gte'],
            'CAYM2_FRS':['lte', 'gte'],
            "About": ['icontains',],
        }