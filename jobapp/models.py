from django.db import models

# Create your models here.
class Jobs(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_posted = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
