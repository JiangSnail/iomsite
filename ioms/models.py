from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Iom(models.Model):
    updator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='修改用户' ,default=1)
    unit = models.CharField(max_length=50,blank = True)
    RFI = models.CharField(max_length=50,blank = True)
    PO_Description = models.CharField(max_length=500,blank = True)
    speciality = models.ForeignKey('Speciality', on_delete = models.SET_NULL,null=True)
    subject = models.ForeignKey('Subject', on_delete = models.SET_NULL,null=True)
    equipment = models.CharField(max_length=1000,blank = True)
    name = models.CharField(max_length=100,blank = True)
    title_Chn = models.CharField(max_length=100,blank = True)
    title = models.CharField(max_length=1000,blank = True)
    originator = models.CharField(max_length=50,blank = True)
    revision = models.CharField(max_length=10,blank = True)
    pdf_file = models.FileField(upload_to='uploads/', blank = True)
    size = models.BigIntegerField(default=0, null=True, blank = True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    document_Date = models.DateField(auto_now_add=True)
    
    

    def __str__(self): 
        return self.name
    class Meta: 
        verbose_name = 'IOM手册' 
        verbose_name_plural = verbose_name
        ordering = ("speciality",)


class Speciality(models.Model):
    speciality = models.CharField(max_length=100)
    speciality_Chn = models.CharField(max_length=50,blank = True)

    class Meta:
        verbose_name = 'speciality'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.speciality

class Subject(models.Model):
    subject = models.CharField(max_length=100)
    subject_Chn = models.CharField(max_length=50,blank = True)
    speciality = models.ForeignKey('Speciality', on_delete = models.CASCADE)
    
    class Meta:
        verbose_name = 'subject'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.subject