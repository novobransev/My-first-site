from django.db import models

class InfoImg(models.Model):
    image = models.ImageField(upload_to='main_page/images/')

class Desc(models.Model):
    description = models.TextField(max_length=260)

class Homework(models.Model):
    title = models.TextField(max_length=260)

class DateNow(models.Model):
    date = models.DateField()

class Title_eveen_week(models.Model):
    title_even = models.CharField(max_length=40, default=None)

class Title_odd_week(models.Model):
    title_odd = models.CharField(max_length=40, default=None)

class Border_even_week(models.Model):
    border_even = models.CharField(max_length=40, default=None)

class Border_odd_week(models.Model):
    border_odd = models.CharField(max_length=40, default=None)