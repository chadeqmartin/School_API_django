from django.db import models
from django.core import validators as v
from .validators import validate_school_email
from .validators import validate_combination_format
from .validators import validate_name_format

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, validators=[validate_name_format])
    student_email = models.EmailField(null=False, blank=False, unique=True, validators=[validate_school_email])
    personal_email = models.EmailField(null=True, blank=True, unique=True)
    locker_number = models.IntegerField(default=110, null=False, blank=False, unique=True, validators=[v.MinValueValidator(1), v.MaxValueValidator(200)])
    locker_combination = models.CharField(max_length=255, default='12-12-12', null=False, blank=False, validators=[validate_combination_format])
    good_student=models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.student_email} - {self.locker_number}"
    
    def locker_reassignment(self, int):
        self.locker_number = int
        self.save()
    
    def student_status(self, bool_val):
        self.good_student = bool_val
        self.save()