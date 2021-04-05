from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.core.validators import MaxValueValidator

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    
    #additional attribute for the user model
    picture = models.ImageField(upload_to='profile_images', blank=True)
    
    def __str__(self):
        return self.user.username
#category data structure  
class Category(models.Model):
    NAME_MAX_LENGTH = 128
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    #slug used so that lower chance of failure of URL mapping
    slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name
#game data structure       
class Game(models.Model):
    TITLE_MAX_LENGTH = 128
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    #slug used so that lower chance of failure of URL mapping
    slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Game, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title
#Review data structure
class Review(models.Model):
    REVIEW_MAX_LENGTH = 2000
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    score = models.IntegerField(validators=[MaxValueValidator(10)])
    comment = models.CharField(max_length=REVIEW_MAX_LENGTH)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = 'Reviews'
    
    def __str__(self):
        return '{} {}'.format(self.game,self.user)