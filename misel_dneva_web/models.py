from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.dispatch import receiver
from django.utils import timezone
from datetime import datetime, timedelta

# Create your models here.

class ModeratorUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #extendamo User-ja
    
    #avtomaticno ustvari model, ko se updejta User
    @receiver(post_save, sender=User)
    def create_registered_user(sender, instance, created, **kwargs):
        if created:
            ModeratorUser.objects.create(user=instance)
    
    #avtomaticno shrani model, ko se updejta User
    @receiver(post_save, sender=User)
    def save_registered_user(sender, instance, **kwargs):
        instance.moderatoruser.save()

class RegisteredUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #extendamo User-ja
    birth_date = models.DateField()                             #shranimo se datum rojstva
    country = models.CharField(max_length=50)                   #in drzavo, iz katere je
    
    #avtomaticno ustvari model, ko se updejta User
    @receiver(post_save, sender=User)
    def create_registered_user(sender, instance, created, **kwargs):
        if created:
            RegisteredUser.objects.create(user=instance)
    
    #avtomaticno shrani model, ko se updejta User
    @receiver(post_save, sender=User)
    def save_registered_user(sender, instance, **kwargs):
        instance.registereduser.save()

class Color(models.Model):
    name = models.CharField(max_length=20)

class Tag(models.Model):
    name = models.CharField(max_length=15)
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True)

class Comment(models.Model):
    author = models.ForeignKey(RegisteredUser, on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')
    report_count = models.IntegerField(validators=[MinValueValidator(0)])

class Thought(models.Model):
    video = models.FileField(upload_to='uploads/profiles/videos')
    title = models.CharField(max_length=50)
    tags = models.ManyToManyField(Tag)
    private = models.BooleanField(default=True)
    pub_date = models.DateTimeField('date published')
    views = models.IntegerField(validators=[MinValueValidator(0)])
    positive_rating = models.IntegerField(validators=[MinValueValidator(0)])
    negative_rating = models.IntegerField(validators=[MinValueValidator(0)])
    comments = models.ManyToManyField(Comment)

class Profile(models.Model):
    registered_user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.FileField(upload_to='uploads/profiles/pictures')
    thoughts = models.ManyToManyField(Thought)
    warned = models.BooleanField(default=False)