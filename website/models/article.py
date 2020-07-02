from django.db import models
from django.urls import reverse
from django.template.defaultfilters import truncatechars

# third part slugify library works better than django's one
# https://github.com/un33k/python-slugify
from slugify import slugify


class Article(models.Model):
    header = models.CharField(max_length=100)
    text = models.TextField(max_length=100000)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    fixed_to_top = models.BooleanField(default=False)

    FEED_SECTIONS = [
        ("WS", "Водогосподарська обстановка"),
        ("EV", "Еколого-просвітницькі заходи"),
        ("MR", "Управління річковими басейнами"),
    ]

    category = models.CharField(
        max_length=10, blank=True, null=True, choices=FEED_SECTIONS
    )
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        kwargs = {"slug": self.slug}
        return reverse("article", kwargs=kwargs)

    def get_category(self):
        category = self.category
        sections = self.FEED_SECTIONS
        ans = list(filter(lambda x: x[0] == category, sections))+[""]
        if ans[0]:
            return tuple(ans[0])[1]
        else:
            return ""

    def save(self, *args, **kwargs):
        value = self.header
        origin_slug = unique_slug = slugify(value)
        numb = 0
        while Article.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{origin_slug}-{numb}'
            numb += 1
        self.slug = unique_slug
        super().save(*args, **kwargs)

    # shortener for an admin list view
    @property
    def short_description(self):
        return truncatechars(self.text, 75)

    def __str__(self):
        return f"{self.header}: {self.text[:20]}"
