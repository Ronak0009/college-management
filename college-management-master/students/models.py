from django.db import models


class Student(models.Model):
     gender_choices=(('M','Male'),('F','Female'),('O','Other'),)
     branch_choices=(('CE','Computer Engineering'),
                       ('IT','Information Technology'),
                       ('EC','Electronics and Comm. Engineering'),
                       ('BME','Bio-Medical Engineering'),
                       ('MC','Mechantronics Engineering'),
                       ('ME','Mechanical Engineering'),
                       ('CE','Civil Engineering'),
                       ('EE','Electrical Engineering'),
                       ('ME','Marine Engineering'),
                       ('AE','Automobile Engineering'),
                       ('PE','Petrochemical Engineering'))    
     sem_choices=(('1','I'),
                    ('2','II'),
                    ('3','III'),
                    ('4','IV'),
                    ('5','V'),
                    ('6','VI'),
                    ('7','VII'),
                    ('8','VIII'))              

     firstName = models.CharField(max_length=70, default='')
     middleName = models.CharField(max_length=70, default='')
     lastName = models.CharField(max_length=70, default='')
     username=models.CharField(max_length=70)
     passwd = models.CharField(max_length=70)
     confirm_passwd = models.CharField(max_length=70)
     confirm_passwd = models.CharField(max_length=70)
     enrollment = models.CharField(max_length=70, primary_key=True)
     date = models.CharField(max_length=70)
     branch = models.CharField(max_length=70)
     mobile=models.CharField(max_length=10)
     branch=models.CharField(max_length=70,choices=branch_choices)
     sem=models.CharField(max_length=5,choices=sem_choices)
     email = models.EmailField(max_length=70)
     
     gender=models.CharField(max_length=7,choices=gender_choices)


