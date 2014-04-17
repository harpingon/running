from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Manufacturer(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

class Shoe(models.Model):
    name = models.CharField(max_length=30)
    purchased = models.DateField()
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    manufacturer = models.ForeignKey(Manufacturer)

    def __unicode__(self):
        return self.name

class Run(models.Model):
    rundate = models.DateField()
    distance = models.DecimalField(max_digits=3, decimal_places=1)
    calories = models.PositiveSmallIntegerField()
    shoe = models.ForeignKey(Shoe)
    notes = models.TextField(blank=True)

    def __unicode__(self):
        return unicode(self.rundate)
