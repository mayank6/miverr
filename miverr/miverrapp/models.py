from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.
class Gig(models.Model):
    CATEGORY_CHOICES=(
    ("GD","Graphic designing"),
    ("DM","Digital Marketing"),
    ("CW","Content-Writing"),
    ("GM","Game & Animation"),
    ("MV","Music and video"),
    )
    title=models.CharField(max_length=500)
    category=models.CharField(max_length=2,choices=CATEGORY_CHOICES)
    description=models.CharField(max_length=1000)
    price=models.IntegerField(default=6)
    photo=models.FileField(upload_to='gigs')
    status=models.BooleanField(default=True)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    create_time=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
