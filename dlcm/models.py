from django.db import models
from django.utils import timezone
from django.db.models.options import Options
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Form(models.Model):
    sub_date = models.DateField('date published')
    def __str__(self):
        return self.sub_date

class Section(models.Model):
    section_name = models.CharField(max_length=200)
    #report_date = models.ForeignKey(Form,on_delete=models.CASCADE)
    #question_text = models.CharField(max_length=200, default= "N/A")
    def __str__(self):
        return self.section_name

class Question(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    question_optional = models.BooleanField(default="False")
    def __str__(self):
        return self.question_text


class Choice(models.Model):
	choice_text = models.CharField(max_length=200,default='NULL')
	question_text = models.ForeignKey(Question,on_delete=models.CASCADE)
	vote = models.CharField(max_length=200, default= 'NULL')


"""
class ChoiceBinary(models.Model):
    #question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.BinaryField(max_length=200)
    #vote = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text"""