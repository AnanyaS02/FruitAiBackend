from django.db import models

# Create your models here.

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    title = models.CharField(max_length=50, default="Tangerine")
    
    def _str_(self):
        return self.question