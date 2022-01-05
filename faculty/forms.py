from django import forms  
class FacultyForm(forms.Form):
    """Form for uploading faculty data sheet to upload new data"""  
    file = forms.FileField(label="Upload the file")

MODEL_FIELDS = [
    ('name', 'name'),
    ('designation', 'designation'),
    ('department', 'department'),
    ('central_responsibility', 'central_responsibility'),
    ('status', 'status'),
    ('date_of_joining', 'date_of_joining'),
    ('mobile_number ', 'mobile_number '),
    ('picture', 'picture'),
    ('CAY_FAP_Score', 'CAY_FAP_Score'),
    ('CAY_Feedback_Score', 'CAY_Feedback_Score'),
    ('CAY_FRP_Score', 'CAY_FRP_Score'),
    ('CAY_FRS', 'CAY_FRS'),
    ('CAYM1_FAP_Score', 'CAYM1_FAP_Score'),
    ('CAYM1_Feedback_Score', 'CAYM1_Feedback_Score'),
    ('CAYM1_FRP_Score', 'CAYM1_FRP_Score'),
    ('CAYM1_FRS', 'CAYM1_FRS'),
    ('CAYM2_FAP_Score', 'CAYM2_FAP_Score'),
    ('CAYM2_Feedback_Score', 'CAYM2_Feedback_Score'),
    ('CAYM2_FRP_Score', 'CAYM2_FRP_Score'),
    ('CAYM2_FRS', 'CAYM2_FRS'),
    ("Faculty_List","Faculty_List"),
    ('About', 'About'),
    ("Search", "Search")
    ]
class FacultyUpdateForm(forms.Form):
    """Form for uploading faculty datasheet to update existing data"""
    Faculty_Id = forms.CharField(label="Faculty Id as in the column")
    field= forms.CharField(label='Choose the field to update', widget=forms.Select(choices=MODEL_FIELDS))
    field_name = forms.CharField(label="Field name as in the sheet")
    file = forms.FileField(label="Upload the file")

class YearUpdateForm(forms.Form):
    """Form for uploading faculty datasheet to update existing data"""
    CAY = forms.CharField(label="Enter the Current Academic Year (CAY) ")
    CAYM1= forms.CharField(label='Enter the Previous Academic Year (CAY-1)')
    CAYM2 = forms.CharField(label="Enter the Previous of Previous Academic Year(CAY-2)")
