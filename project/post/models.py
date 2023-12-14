from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'


class Category(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
# Create your models here.
