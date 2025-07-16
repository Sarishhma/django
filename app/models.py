from django.db import models
from django.utils import timezone

# Create your models here.
class item(models.Model):
    ITEM_CHOICES =[
        ('EL', 'Electronics'),
        ('CL', 'Clothing'),
        ('BL', 'Books'),
        ('HL', 'Home Appliances'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    date_added= models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2,choices=ITEM_CHOICES)
    def __str__(self):
        return self.name