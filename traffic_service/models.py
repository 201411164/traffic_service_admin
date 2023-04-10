from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, username, password, **kwargs):
        if not username:
            raise ValueError("Username is required")
        if not password:
            raise ValueError("Password is required")

        user = self.model(username=username, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **kwargs):
        user = self.create_user(username, password, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50, null=True)
    phone_number = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(default=datetime.utcnow)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_code = models.CharField(max_length=50, default='normal')
    user_nvmid = models.CharField(max_length=50, null=True)
    keyword = models.CharField(max_length=50, null=True)
    is_mobile = models.BooleanField(default=False)
    is_shopping = models.BooleanField(default=False)
    is_grouped_item = models.BooleanField(default=False)
    start_date = models.DateTimeField(default=datetime.utcnow)
    end_date = models.DateTimeField(default=datetime.utcnow)
    price = models.FloatField(default=0.0)
    is_turned_on = models.BooleanField(default=False)
    today_hitcount = models.IntegerField(default=0)
    total_hitcount = models.IntegerField(default=0)

class Log(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='logs')
    is_mobile = models.BooleanField(default=False)
    is_shopping = models.BooleanField(default=False)
    ip_address = models.CharField(max_length=50)
    access_time = models.DateTimeField(default=datetime.utcnow)
    access_url = models.CharField(max_length=50)
    keyword = models.CharField(max_length=50)
    user_nvmid = models.CharField(max_length=50)
    stay_time = models.IntegerField(default=0)

class Admin(models.Model):
    target_daily_hitcounts = models.IntegerField(default=150, null=True)
