from django.db import models


class Launche(models.Model):
    data = models.TextField()

    def __str__(self):
        return self.data
