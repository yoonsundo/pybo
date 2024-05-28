from django.db import models

# Create your models here.
class CodeList(models.Model): 
    codegbncd = models.CharField(max_length=20)
    codegbnnm = models.CharField(max_length=20)
    codegbnengnm = models.CharField(max_length=20, null=True, blank=True) 
    codegrpcd = models.CharField(max_length=20)
    upcodecd = models.CharField(max_length=20, null=True, blank=True)
    remark1 = models.CharField(max_length=20, null=True, blank=True)
    remark2 = models.CharField(max_length=20, null=True, blank=True)
    remark3 = models.CharField(max_length=20, null=True, blank=True)
    remark4 = models.CharField(max_length=20, null=True, blank=True)
    codeseq = models.CharField(max_length=20, null=True, blank=True)
     

    class Meta:
        verbose_name = '공통코드'
        verbose_name_plural = '공통코드'
        ordering = ['-codegbncd', ]
    
    def __str__(self):
        return self.codegbnnm