from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    CHOICES = (
        ('A','PYTHON'),
        ('B','DJANGO')
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=70,help_text='enter title',unique=True,db_column='mytitle',editable=False)
    body = models.TextField(choices=CHOICES)
    image = models.ImageField(upload_to='images/articles',unique_for_date='pop_date')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    pop_date = models.DateField(default=timezone.now())


    def __str__(self):
        return self.title+ "-" + self.body

