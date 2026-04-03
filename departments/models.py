from django.db import models
from django.contrib.auth.models import User 

class Department(models.Model):
    user = models.ForeignKey(User,  on_delete=models.CASCADE) 



    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True , null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name