from django.db import models

# Create your models here.
class Coding_question(models.Model):
    question = models.CharField(max_length=250)
    status = models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.question

class Noncoding_question(models.Model):
    question = models.CharField(max_length=250)

    def __str__(self):
        return self.question


class Intern(models.Model):
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    completed_course = models.CharField(max_length=250)
    year_of_passout = models.CharField(max_length=250)
    college = models.CharField(max_length=250)
    mobile_no = models.IntegerField()
    technologies = models.CharField(max_length=250)
    interested_field = models.CharField(max_length=20)

    def __str__(self):
        return self.id

class Message(models.Model):
    phone = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    content = models.CharField(max_length=250)
    mail = models.CharField(max_length=250)
    objects = models.Manager()

class Result(models.Model):
    student_id = models.CharField(max_length=250)
    ques_name = models.CharField(max_length=250)
    ques_ans = models.CharField(max_length=250)
    objects = models.Manager()