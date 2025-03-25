from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        # Ensure superuser has default values for required fields
        if 'phone_number' not in extra_fields or not extra_fields['phone_number']:
            extra_fields['phone_number'] = "9840422664"  # Default phone number
        
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)  # Ensure is_superuser is included
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    phone_number = models.CharField(max_length=15, unique=True)
    address = models.TextField()
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    # Implementing the required permissions methods
    def has_perm(self, perm, obj=None):
        # Return True or False if the user has the permission.
        return self.is_superuser

    def has_module_perms(self, app_label):
        # Return True or False if the user has permission to view the app.
        return self.is_superuser


# Blog Model
class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)

    def __str__(self):
        return self.title


# AgroMart Models for Business and Farmer
class Business(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=255)
    contact = models.CharField(max_length=15)
    business_image = models.ImageField(upload_to='business_images/', null=True, blank=True)

    def __str__(self):
        return self.business_name


class Product(models.Model):
    business = models.ForeignKey(Business, related_name="products", on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_available = models.IntegerField()
    product_image = models.ImageField(upload_to='product_images/', null=True, blank=True)

    def __str__(self):
        return self.product_name


class Farmer(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    quantity = models.CharField(max_length=50)
    contact = models.CharField(max_length=15)
    farmer_image = models.ImageField(upload_to='farmer_images/', null=True, blank=True)

    def __str__(self):
        return self.product_name


# Community Post Model
class CommunityPost(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='community_images/', null=True, blank=True)

    def __str__(self):
        return f'Post by {self.user.email}'


# Comment and Reactions for Community Posts
class Comment(models.Model):
    post = models.ForeignKey(CommunityPost, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.email}'


class Reaction(models.Model):
    post = models.ForeignKey(CommunityPost, on_delete=models.CASCADE, related_name='reactions')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    reaction_type = models.CharField(max_length=50)

    def __str__(self):
        return f'Reaction by {self.user.email}'

