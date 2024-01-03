from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Courses(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    son = models.IntegerField()
    img = models.ImageField(upload_to='Courses/img')

    def get_absolute_url(self):
        return reverse("coursedetail", args=[self.slug])

    def __str__(self):
        return self.name

class Courses1(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    son = models.IntegerField()
    img = models.ImageField(upload_to='Courses/img')

    def __str__(self):
        return self.name

class Popcourses(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    shaxs = models.CharField(max_length=100)
    son = models.IntegerField()
    img = models.ImageField(upload_to='Popcourses/img')

    def __str__(self):
        return self.name

class Experts(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    bio = models.TextField()
    img = models.ImageField(upload_to='Experts/img')

    def get_absolute_url(self):
        return reverse("expertdetail", args=[self.slug])

    def __str__(self):
        return self.name

class Aboutus(models.Model):
    bio = models.TextField()
    img = models.ImageField(upload_to="Aboutus/img")

    def __str__(self):
        return self.name

class Experts1(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    img = models.ImageField(upload_to='Experts/img')

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    massage = models.TextField()

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length=100)
    comment = models.TextField()
    img = models.ImageField(upload_to='Testimonial/img')

    def __str__(self):
        return self.name











