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
    ('FAP_1920_Score', 'FAP_1920_Score'),
    ('Feedback_1920_Score', 'Feedback_1920_Score'),
    ('FRP_1920', 'FRP_1920'),
    ('FRS_1920', 'FRS_1920'),
    ('FAP_2021_Score', 'FAP_2021_Score'),
    ('Feedback_2021_Score', 'Feedback_2021_Score'),
    ('FRP_2021', 'FRP_2021'),
    ('FRS_2021', 'FRS_2021'),
    ('FAP_2122_Score', 'FAP_2122_Score'),
    ('Feedback_2122_Score', 'Feedback_2122_Score'),
    ('FRP_2122', 'FRP_2122'),
    ('FRS_2122', 'FRS_2122'),
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
