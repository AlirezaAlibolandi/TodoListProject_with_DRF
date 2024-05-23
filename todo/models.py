from django.db import models


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    priority = models.IntegerField(default=5)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'todo'
