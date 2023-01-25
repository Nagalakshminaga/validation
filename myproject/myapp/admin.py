from django.contrib import admin

# Register your models here.
from .models import CommentModel

admin.site.register(CommentModel)