from django.db import models

# Create your models here.
class Movies(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True,blank=True,upload_to="images/")
    ratings = models.IntegerField()


    def __str__(self):
        return str(self.title)
    
    # def get_absolute_url(self):
    #     return reverse('home')