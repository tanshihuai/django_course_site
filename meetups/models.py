from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name}, {self.location}'

class Participant(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

class Meetup(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='images')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    participants = models.ManyToManyField(Participant, blank=True, null=True)
    organizer_email = models.EmailField()
    date = models.DateField()

    