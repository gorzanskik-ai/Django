from django.db import models

# Create your models here.

class Film(models.Model):
    title = models.CharField(max_length=64, blank=False, unique=True)
    year = models.PositiveIntegerField(blank=False, default=2000)
    description = models.TextField(default='')
    premiere = models.DateField(null=True, blank=True)
    imdb_rating = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    poster = models.ImageField(upload_to='posters', null=True, blank=True)

    def __str__(self):
        return self.title + ' (' + str(self.year) + ')'
    
    def title_year(self):
        return f"{0} ({1})".format(self.title, self.year)
