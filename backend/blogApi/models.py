from django.db import models

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class blog(models.Model):
    category = models.ForeignKey(category, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    excerpt = models.CharField(max_length=255, default='') 
    content = models.TextField(null=True, blank=True)
    contentTwo = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='image', null=True, blank=True)
    ingredients = models.TextField(null=True, blank=True)   
    
    def __str__(self):
        return self.title