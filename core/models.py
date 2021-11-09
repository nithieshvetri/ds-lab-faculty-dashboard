from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin
from django.core.validators import RegexValidator


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError("Users must have an email address")
        email = email.lower()
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class Faculty(models.Model):
    """Faculty model"""
    class Meta:
        ordering = ('faculty_id',)
        verbose_name_plural = "Faculty"


    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

    faculty_id = models.CharField(max_length=100,
                                  validators=[alphanumeric,],
                                  verbose_name="Faculty Id")
    name = models.CharField(max_length=255, default=None, verbose_name="Faculty Name")
    designation = models.CharField(max_length=255, default=None, verbose_name="Designation")
    department = models.CharField(max_length=255, default=None, verbose_name="Department")
    central_responsibility=models.CharField(max_length=100, null=True, default=None, verbose_name="Central Responsibility")
    status=models.CharField(max_length=50, default=None, null=True, verbose_name="Status")
    date_of_joining = models.DateField(default=None, null=True, verbose_name="Date of Joining")
    mobile_number = models.CharField(max_length=20, null=True, default=None,verbose_name="Mobile Number")
    email = models.EmailField(verbose_name="E-Mail")
    picture = models.URLField(max_length=400, default=None,null=True, verbose_name="Image")
    FAP_1920_Score = models.DecimalField(max_digits=4, decimal_places=2, null=True,blank=True, default=None, verbose_name="FAP 19-20 Score")
    Feedback_1920_Score = models.DecimalField(max_digits=3, decimal_places=2, null=True,blank=True, default=None, verbose_name="Feedback 19-20 Score")
    FRP_1920 = models.DecimalField(max_digits=3, decimal_places=2, null=True,blank=True, default=None, verbose_name="FRP 19-20")
    FRS_1920 = models.DecimalField(max_digits=6, decimal_places=0, blank=True, default=None, null=True,verbose_name="FRS 19-20")
    FAP_2021_Score = models.DecimalField(max_digits=4, decimal_places=2, null=True,blank=True, default=None, verbose_name="FAP 20-21 Score")
    Feedback_2021_Score = models.DecimalField(max_digits=3, decimal_places=2, null=True,blank=True, default=None, verbose_name="Feedback 20-21 Score")
    FRP_2021 = models.DecimalField(max_digits=3, decimal_places=2, null=True,blank=True, default=None, verbose_name="FRP 20-21")
    FRS_2021 = models.DecimalField(max_digits=6, decimal_places=0, blank=True, default=None, null=True,verbose_name="FRS 20-21")
    FAP_2122_Score = models.DecimalField(max_digits=4, decimal_places=2, null=True,blank=True, default=None, verbose_name="FAP 21-22 Score")
    Feedback_2122_Score = models.DecimalField(max_digits=3, decimal_places=2, null=True,blank=True, default=None, verbose_name="Feedback 21-22 Score")
    FRP_2122 = models.DecimalField(max_digits=3, decimal_places=2, null=True,blank=True, default=None, verbose_name="FRP 21-22")
    FRS_2122 = models.DecimalField(max_digits=6, decimal_places=0, blank=True, default=None, null=True,verbose_name="FRS 21-22")
    Faculty_list = models.TextField(max_length=500, null=True, default=None, verbose_name="Faculty List")
    About = models.TextField(max_length=500, null=True, default=None, verbose_name="About")
    Search = models.TextField(max_length=500, null=True, default=None, verbose_name="Search")
    def __str__(self):
        return self.faculty_id

