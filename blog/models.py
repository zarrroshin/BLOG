from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse




class Category(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True,null=False,default='')


    def __str__(self):
        return self.name



class ArticleManager(models.Manager):
    def counter(self):
        return len(self.all())
    def status(self):
        return self.filter(status=True)
    def get_queryset(self):
        return super().get_queryset().filter(status=True)



class Article(models.Model):
    CHOICES = (
        ('A','PYTHON'),
        ('B','DJANGO')
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category,related_name='articles')
    title = models.CharField(max_length=70,help_text='enter title',unique=True)
    body = models.TextField(choices=CHOICES)
    image = models.ImageField(upload_to='images/articles',unique_for_date='pop_date')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    pop_date = models.DateField(default=timezone.now())
    floatfield = models.FloatField(default=0)
    myfile = models.FileField(null=True,upload_to='files/articles')
    status = models.BooleanField(default=False)
    objects = models.Manager()
    custom = ArticleManager()
    slug = models.SlugField(unique=True,null=True,blank=True)

    class Meta:
        ordering = ['-updated',]
        verbose_name = 'post'


    def __str__(self):
        return self.title+ "-" + self.body


    def save(self, *args, **kwargs):
        self.slug = self.title
        super(Article,self).save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse('blog:article_detail',kwargs={'slug':self.slug})


# class New(models.Model):
#     title= models.CharField(max_length=70)
#     des = models.TextField()
#
#     def __str__(self):
#         return self.title
#
#     def save(self, *args, **kwargs):
#         self.title = self.title.replace(" ","*")
#         super(New,self).save(*args, **kwargs)