from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "categories"
    def __str__(self):
        return str(self.name)

class Post(models.Model):
    title = models.TextField()
    author = models.CharField(max_length = 255)
    #body = models.TextField()
    body = RichTextField(blank=True, null= True)
    created_on = models.DateTimeField(auto_now_add = True)
    categories = models.ManyToManyField("Category",related_name="posts")

    def __str__(self):
        return str(self.title)

class comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post",on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.author} on '{self.post}'"
