from django.db import models

# Create your models here.
#signup for email subscribe
class Signup(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

#work for contact registration

class Contact(models.Model):
    
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    msg = models.TextField(max_length=400, blank=True)

    def __str__(self):
        return self.name

