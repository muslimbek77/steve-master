from django.contrib import admin
from .models import Contact, Blog, Category

admin.site.register(Contact)
admin.site.register(Category)
admin.site.register(Blog)
