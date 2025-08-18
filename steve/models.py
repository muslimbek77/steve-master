from django.db import models
from django.utils.text import slugify

class Contact(models.Model):
    name = models.CharField(max_length=255)
    message = models.TextField()
    email = models.EmailField()
    subject = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, null=True)
    photo = models.ImageField(upload_to='Blog/')
    content = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,blank=True,null=True)
    created_date = models.DateField(auto_now=True)
    author = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title