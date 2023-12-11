from django.db import models

# Create your models here.


class  Article(models.Model):
    title=models.CharField(max_length=255)
    slug=models.SlugField()
    body=models.TextField()
    date=models.TimeField(auto_now_add=True)
    thumb=models.ImageField(default='default.png',blank=True)

    def __str__(self) -> str:
        return self.title


    def snippet(self):
        return self.body[:50]+'........'







