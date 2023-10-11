from django.db import models

# Create your models here.
class Book(models.Model):
    GENRE = (
        ('Genre','genre'),
        ('Fantasy', 'fantasy'),
        ('Detective', 'detective')
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    cost = models.IntegerField()
    created_date = models.DateTimeField(auto_created=True)
    author = models.CharField(max_length=100, null=True)
    genre = models.CharField(max_length=100, choices=GENRE, default=GENRE[0], null=True)

    def __str__(self):
        return self.title