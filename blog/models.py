from django.db import models
from django.utils import timezone


class Post(models.Model):
    yazar = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    baslik = models.CharField(max_length=200)
    yazi = models.TextField()
    tarihOlusturma = models.DateTimeField(
            default=timezone.now)
    tarihYayinlama = models.DateTimeField(
            blank=True, null=True)

    def yayinla(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.baslik