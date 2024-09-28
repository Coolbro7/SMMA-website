from django.contrib import admin
from blogs.models import category,comment,Post
# Register your models here.
admin.site.register(category)
admin.site.register(comment)
admin.site.register(Post)