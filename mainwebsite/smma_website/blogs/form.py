from django.forms import ModelForm
from .models import *

class BlogCreate(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'