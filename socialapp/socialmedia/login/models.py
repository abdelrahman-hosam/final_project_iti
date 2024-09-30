from django.db import models
from django.contrib.auth.hashers import make_password, check_password
class customuser(models.Model):
    username = models.CharField(max_length=200 , unique=True , primary_key= True)
    password = models.CharField(max_length=128)
    def set_password(self , raw_password):
        self.password = make_password(raw_password)
    def check_password(self , raw_password):
        return check_password(raw_password , self.password)
    def save(self, *args, **kwargs):
        if self.pk is None: 
            self.set_password(self.password)
        super().save(*args, **kwargs)
    @classmethod
    def create_user(cls , username , password):
        user = cls(username=username)
        user.set_password(password)
        user.save()
        return user
        
    