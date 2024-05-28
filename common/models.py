from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile') 
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)

    class Meta:
        verbose_name = '사용자'
        verbose_name_plural = '사용자추가정보'
        ordering = ['-name', ]
    
    def __str__(self):
        return self.name

 