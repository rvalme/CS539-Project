from django.db import models

# Create your models here.
class ZipStarbuck(models.Model):
    zipcode = models.CharField(max_length=50, unique=True)
    num_sb = models.CharField(max_length=50)

    def __str__(self):
        return self.zipcode


