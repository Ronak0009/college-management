from django.db import models

# Create your models here.
class AppUser(models.Model):
    categories = (('Student', 'Student'),
                ('Faculty','Faculty'),
                ('Staff','Staff'),
                ('Admin','Admin'),
                ('Head of Department','Head of Department'))

    firstName = models.CharField(max_length=70,
                     default='',
                    verbose_name="First Name")

    lastName = models.CharField(max_length=70,
                    default='',
                    verbose_name="Last Name")

    username=models.CharField(max_length=70,
                    verbose_name="Username",
                    primary_key=True, unique=True)

    passwd = models.CharField(max_length=70,
                    verbose_name="Password")
    
    email = models.EmailField(max_length=70,
                    verbose_name="Email")

    category = models.CharField(max_length=70,
                    verbose_name="User Category",
                    choices=categories)

    isAdmin=models.BooleanField(max_length=10,
                    default=False)

    isPending = models.BooleanField(max_length=10,
                    default=True)
