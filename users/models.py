from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField



class accountManager(BaseUserManager):
    
    def create_user(self,idno,email,password=None):
        if not email:
            raise ValueError('Email is a required')    
        
        user=self.model(
            email=self.normalize_email(email),
            idno=idno,
            
        )
        user.is_superuser=True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,idno,password):     
                
        user=self.create_user(
            email=self.normalize_email(email),
            password=password,
            idno=idno,
            )

        user.is_staff=True
        user.is_superuser=True
        user.is_active=True 

        
        user.save(using=self._db)
        return user

class users(AbstractBaseUser,PermissionsMixin):
    idno=models.IntegerField(primary_key=True)
    firstName=models.CharField(max_length=50)
    lastName=models.CharField(max_length=50)
    phone_No=PhoneNumberField()
    address=models.CharField(max_length=100)
    country=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=100)
    date_joined=models.DateField(auto_now_add=True)
    lastLogin=models.DateField(auto_now_add=True)
    is_active=models.BooleanField(default=True)
    is_sponsor=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_student=models.BooleanField(default=False)
    

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['idno','password']

    objects=accountManager()


    def __str__(self):
        return str(self.email)

    def has_perm(self,perm, obj=None):
        return self.is_superuser
    def has_module_perm(self, app_label):
            return True
        
# signal to create a Token for a user when a new user is created
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)   

    # to create tokens for users who existed before implementation of token authentication
    for user in users.objects.all():
        Token.objects.get_or_create(user=user)