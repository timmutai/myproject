from email.mime import image
from django.db import models
from users.models import users

# Create your models here.
class album(models.Model):
    user=models.ForeignKey(users, on_delete=models.PROTECT)
    album=models.CharField(max_length=20, null= False, blank= False )
    

    def __str__(self):
        return self.album
class Gallery(models.Model):
    user=models.ForeignKey(users, on_delete=models.PROTECT)
    album=models.ForeignKey(album, on_delete=models.PROTECT )
    image=models.ImageField(null=False, blank=False)
    caption=models.TextField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.caption