from django.contrib.auth.models import AbstractUser
from django.db import models 


class CustomUser(AbstractUser):
    favorites = models.ManyToManyField('Series', blank=True, related_name='favorited_by')

    def __str__(self):
        return self.username

class ProductionCompany(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Streaming(models.Model):
    platform = models.CharField(max_length=255)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.platform

class MainCast(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.role})" if self.role else self.name

class Series(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    release_date = models.DateField()
    episodes = models.PositiveIntegerField(default=0) 
    short_summary = models.TextField(blank=True, null=True)

    production_company = models.ForeignKey(
        ProductionCompany,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    main_cast = models.ManyToManyField(MainCast, blank=True)
    streaming = models.ManyToManyField(Streaming, blank=True)
    image = models.ImageField(upload_to='series/', null=True, blank=True)

    def __str__(self):
        return self.title

