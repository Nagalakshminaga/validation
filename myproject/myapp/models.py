from django.db import models

# Create your models here.
class CommentModel(models.Model):
	name = models.CharField( max_length = 100, blank = False,null = False)
	comment = models.TextField(blank = False, null = False)
	time = models.DateTimeField(auto_now_add = True)

    
	
	def __str__(self):
         return self.name
