from django.db import models

class RealEstate(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    average = models.DecimalField(max_digits=10, decimal_places=2)
    source_url = models.URLField()
    image_url = models.URLField()
    
    def __str__(self):
        return self.title