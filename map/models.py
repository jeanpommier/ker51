# from django.db import models
from django.contrib.gis.db import models

class Person(models.Model):
    names = models.CharField('Nom(s)', max_length=200)
    fulladdress = models.TextField('Adresse', blank=True, default='')
    location = models.PointField('Lieu', blank=True, null=True, )
    phones = models.CharField('Téléphone(s)', max_length=200, blank=True, default='')
    emails = models.CharField('email(s)', max_length=200, blank=True, default='')
    comments = models.TextField('Commentaires', blank=True, default='')
    picture = models.ImageField('photo', upload_to='trognes/', blank=True, default='')
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return "%s" % (self.names)