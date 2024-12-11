from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    father_name = models.CharField(max_length=50,primary_key=True)
    melicode = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/profiles',blank=True,null=True)


    def __str__(self):
       return self.user.username


    class Meta:
        verbose_name = 'حساب کاربری '
        verbose_name_plural = 'حساب های کاربری'