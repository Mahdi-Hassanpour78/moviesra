from django.db import models


class MoviesModel(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    summery = models.TextField()
    LANGUAGE_CHOICES = [
        ('EN','ENGLISH'),
        ('PR','PERSIAN'),
        ('GR','GERMANY'),
    ]
    lang = models.CharField(
        max_length=3,
        choices=LANGUAGE_CHOICES, 
        default='EN' )
    COUNTRY_CHOICES = [ 
        ('US','UNITED STATES'), 
        ('UK','UNITED KINGDOM'), 
        ('IR','IRAN'), 
        ('GR','GERMANY'), 
        ]
    country = models.CharField( 
        max_length=3, 
        choices=COUNTRY_CHOICES, 
        default='US' 
        )
    GENRE_CHOICES = [ 
        ('AC','ACTION'), 
        ('DR','DRAMA'), 
        ('HR','HORROR'), 
        ]
    genre = models.CharField( 
        max_length=3, 
        choices=GENRE_CHOICES, 
        default=None 
        )
    AGES_CHOICES = [ 
        ('G','GENERAL'), 
        ('PG','PARENTAL GUIDANCE'), 
        ('R','RESTRICTED'), 
        ]
    ages = models.CharField( 
        max_length=3, 
        choices=AGES_CHOICES, 
        default=None 
        )


class CastModel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    image = models.ImageField()
    born = models.DateField()
    social_media = models.URLField()
    #role = models.CharField()
