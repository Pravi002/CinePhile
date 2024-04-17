from django.db import models
from django.contrib.auth.models import User


LANGUAGE_CHOICES=(
    ('malayalam','MALAYALAM'),('tamil','TAMIL'),('english','ENGLISH'),('telugu','TELUGU'),('kannada','KANNADA'),
    ('hindi','HINDI'),('korean','KOREAN'),('french','FRENCH'),('germen','GERMEN'),('chinese','CHINESE'),('japanese','JAPANESE'))

GENRE_CHOICES=(('action','ACTION'),('sci-fi','SCI-FI'),('comedy','COMEDY'),('thriller','THRILLER'),
               ('horror','HORROR'),('drama','DRAMA'),('war','WAR'),('historic','HISTORIC'),
               ('documentary','DOCUMENTARY'),('fantasy','FANTASY'),('crime','CRIME'),('sports','SPORTS'),
               ('music','MUSIC'),('romance','ROMANCE'),('animation','ANIMATION'),('slasher','SLASHER'),
               ('adventure','ADVENTURE'),('mystery','MYSTERY'),('survival','SURVIVAL'),('family','FAMILY'))

STATUS_CHOICES=(('MP','MOST-POPULAR'),('TR','TOP-RATED'),('MA','MOST-ANTICIPATED'),('SH','SUPER-HIT'),
                ('CS','COMING-SOON'),('EG','EVER-GREEN'),('cL','CLASSIC'),('BB','BLOCK-BUSTER'))


class Movie(models.Model):
    title=models.CharField(max_length=50)
    discription=models.TextField()
    image=models.ImageField(upload_to='movie_images')
    genre=models.CharField(choices=GENRE_CHOICES,max_length=20)
    language=models.CharField(choices=LANGUAGE_CHOICES,max_length=20)
    status=models.CharField(choices=STATUS_CHOICES,max_length=20)
    Director=models.CharField(max_length=50)
    cast=models.CharField(max_length=500)
    year=models.DateField(null=True)
    plot=models.TextField(null=True)
    views=models.IntegerField(default=0)


    def __str__(self):
        return self.title
    

class WatchList(models.Model):
    item=models.ForeignKey(Movie,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)


class Diary(models.Model):
    item=models.ForeignKey(Movie,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)

