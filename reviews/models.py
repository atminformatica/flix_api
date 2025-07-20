from django.db import models
from movies.models import Movie

from django.core.validators import MinValueValidator,MaxValueValidator

class Review(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.PROTECT,
        related_name='reviews'
    )
    stars = models.IntegerField(
        validators=[
            MinValueValidator(0,'Não pode ser inferior a zero estrelas.'),
            MaxValueValidator(5,'Não pode ser superior a 5 estrelas.'),
        ]
    )
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.movie.title