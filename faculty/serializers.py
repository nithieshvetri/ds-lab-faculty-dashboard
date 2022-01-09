from django.utils.translation import ugettext_lazy as _
# from core.admin import Yearupdate

from rest_framework import serializers

from core.models import Faculty,Yearupdate


class FacultySerializer(serializers.ModelSerializer):
    """Serializer for listing faculties"""
    class Meta:
        model = Faculty
        fields = '__all__'

class YearSerializer(serializers.ModelSerializer):
    """Serializer for year API"""
    class Meta:
        model = Yearupdate
        fields = '__all__'