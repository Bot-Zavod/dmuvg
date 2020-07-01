from django.db import models
from django.urls import reverse

# third part slugify library works better than django's one
# https://github.com/un33k/python-slugify
from slugify import slugify


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class Article(models.Model):
    header = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateField(auto_now=False, auto_now_add=True)
    fixed_to_top = models.BooleanField(default=False)
    image = models.ImageField(height_field=None, width_field=None, max_length=None)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug
        }
        return reverse('article', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.header
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.header}: {self.text[0:20]}"
