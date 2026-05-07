from django.db import models


class BookTable(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=55)
    phone = models.CharField(blank=False, max_length=20)
    date = models.CharField(blank=False, max_length=15)
    time = models.CharField(blank=False, max_length=12)
    people = models.IntegerField(blank=False, null=False)
    message = models.TextField(max_length=255)

    def __str__(self):
        return self.name


class Qrcode(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=55)
    phone = models.CharField(blank=False, max_length=20)
    date = models.CharField(blank=False, max_length=15)
    time = models.CharField(blank=False, max_length=12)
    people = models.IntegerField(blank=False, null=False)
    message = models.TextField(max_length=255)

    def __str__(self):
        return self.name
