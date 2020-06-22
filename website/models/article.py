from django.db import models


class Article(models.Model):
    header = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateField(auto_now=False, auto_now_add=True)
    fixed_to_top = models.BooleanField(default=False)
    image = models.ImageField(height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return f"{header}: {text[0:20]}"
