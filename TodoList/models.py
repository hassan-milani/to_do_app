from django.db import models

# Create your models here.


class Todo(models.Model):
    item = models.CharField(max_length=500)
    added_date = models.DateTimeField()

    def __str__(self):
        return self.item

