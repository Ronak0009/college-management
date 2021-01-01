from django.db import models


class staff1(models.Model):
     gender_choices=(('M','Male'),('F','Female'),('O','Other'),)
     college_choices=(('Uvpce','U.V Patel College of Engineering'),
                       ('Bspp','B.S Patel Polytechnic'),)
     branch_choices=(('Ce','Computer Engineering'),
                       ('It','Information Technology '),)    
     sem_choices=(('1','I'),
                       ('2','II'),
                       ('3','III'),)              

     fullname = models.CharField(max_length=70)
     username=models.CharField(max_length=70)
     passwd = models.CharField(max_length=70)
     confirm_passwd = models.CharField(max_length=70)
     confirm_passwd = models.CharField(max_length=70)
     enrollment = models.CharField(max_length=70)
     date = models.CharField(max_length=70)
     branch = models.CharField(max_length=70)
     mobile=models.CharField(max_length=10)
     college=models.CharField(max_length=70,choices=college_choices)
     branch=models.CharField(max_length=70,choices=branch_choices)
     sem=models.CharField(max_length=5,choices=sem_choices)
     email = models.EmailField(max_length=70)
     
     gender=models.CharField(max_length=7,choices=gender_choices)






# Create your models here.


# Create your models here.
