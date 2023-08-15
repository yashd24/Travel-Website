from django.db import models


class places(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='static')
    desc = models.TextField()
    amt = models.IntegerField()
    offer = models.BooleanField(default=False)

    def __str__(self):
        return self.name
