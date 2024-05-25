from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    priority = models.IntegerField(default=5)
    done = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'todo'

