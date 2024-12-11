from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model
from django.utils import timezone
from django.urls import reverse
from django.utils.html import format_html

class Category(models.Model):
    name = models.CharField(max_length=50,verbose_name="عنوان")
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True,null=False,default='')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'دسته بندی '



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
    #body = models.TextField(choices=CHOICES)
    body = models.TextField()
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
    pub_date = models.DateField(default=timezone.now())

    class Meta:
        ordering = ['-updated',]
        verbose_name = 'post'


    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        self.slug = self.title
        super(Article,self).save(*args, **kwargs)


    def show_image(self):
        if self.image:
            return format_html(f'<img src="{self.image.url}" width="60px" height="50px">')
        return format_html('<h3 style="color:red">تصویر ندارد </h3>')
    def get_absolute_url(self):
        return reverse('blog:article_detail',kwargs={'slug':self.slug})

  #  def print_title(self):
     #  return  self.title

 #   print_title.short_description = "چاپ عنوان "

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

class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,related_name='comments')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='comments')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    parent  = models.ForeignKey('self',null=True,blank=True,related_name='replies',on_delete=models.CASCADE)

    def __str__(self):
        return self.body[:50]


class Message(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    email = models.EmailField(max_length=70)
    # age = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    # date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

