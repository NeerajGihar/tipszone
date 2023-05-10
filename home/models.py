from django.db import models

class contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=100)
    content = models.TextField(default="")
    timestamp = models.DateField(auto_now_add=True,blank=True)
    
    def __str__(self):
        return 'message from ' + self.name