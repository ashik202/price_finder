from django.db import models
from django.contrib.auth.base_user import BaseUserManager,AbstractBaseUser

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, password=None, mobile_no=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
        if not mobile_no:
            raise ValueError('Users must have a mobile number')

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            first_name=first_name,
            last_name=last_name,
            mobile_no=mobile_no
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, last_name, password, mobile_no=None):
        if not mobile_no:
            raise ValueError('Superusers must have a mobile number')

        user = self.create_user(
            email=email,
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            mobile_no=mobile_no
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user 


class Account(AbstractBaseUser):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    username=models.CharField(max_length=50,default='')
    mobile_no = models.IntegerField()
    email = models.EmailField(max_length=50,unique=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name','username','mobile_no']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True
    
class Url(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    url = models.CharField( max_length=500)
    bying_price = models.IntegerField(default=0)