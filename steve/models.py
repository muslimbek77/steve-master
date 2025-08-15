from django.db import models


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
    photo = models.ImageField(upload_to='Blog/')
    content = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,blank=True,null=True)
    created_date = models.DateField(auto_now=True)
    author = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title