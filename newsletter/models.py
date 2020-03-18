from django.db import models

# Create your models here.
class SignUp(models.Model):
    email     = models.EmailField()
    full_name = models.CharField(max_length=120, blank=True, null=True) #blank-in the form, null-in the db
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated   = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):  #for python 3.3 is __str__, python < 3.3 __unicode__
        return self.email
