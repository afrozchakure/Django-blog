from django.contrib import admin
from .models import Post
# Register your models here.
admin.site.register(Post)  # To make our model visible on the admin page, we need to register the model
