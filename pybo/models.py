from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    question_hit = models.PositiveIntegerField(default=0)
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_question')  # 추천인 추가

    def __str__(self):
        return self.subject
    
    @property
    def update_counter(self):
        self.question_hit = self.question_hit + 1
        self.save()
        return ""

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')

class SideMenuList(models.Model):
    title = models.CharField(max_length=200)
    Level = models.DecimalField(max_digits=5, decimal_places=0) 
    seq = models.DecimalField(max_digits=5, decimal_places=0) 

class SideSubMenuList(models.Model):
    title = models.CharField(max_length=200)
    Level = models.DecimalField(max_digits=5, decimal_places=0) 
    seq = models.DecimalField(max_digits=5, decimal_places=0) 
