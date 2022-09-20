from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.

class tag(models.Model):
    name = models.CharField(max_length=15, null=True)
    
    def __str__(self):
        return self.name


class post(models.Model):
    CATEGORY = (
            ('TECH', 'TECH'),
            ('PYTHON', 'PYTHON'),
            ('JAVA', 'JAVA'),
            ('PROGRAMMING', 'PROGRAMMING'),
        )
    STATUS = (
        (0,"Draft"),
        (1,"Publish")
                )

    title = models.CharField(max_length=255, null=True)
    slug = models.SlugField( max_length=200, unique=True, null=True )
    thumbnail = models.ImageField(null=True, upload_to='photos/')
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    sub_article = models.TextField(max_length=255, null=True)
    article = RichTextUploadingField(null=True)
    category = models.CharField(max_length=50, null=True, choices=CATEGORY)
    tags = models.ManyToManyField(tag)
    status = models.IntegerField(choices=STATUS, default=0, null=True)

    def __str__(self):
        return self.title

class newsletter(models.Model):
    email = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.email

class contact(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    subject = models.CharField(max_length=255, null=True)
    message = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.name