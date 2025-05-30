from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    statution = models.BooleanField(default=True)
    views = models.IntegerField()
    image = models.ImageField(null=True , upload_to="codeyad")


    def __str__(self):
       return f"{self.title} - {self.description[:11]} "