# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Task(models.Model):
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='task', )
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    # TODO: добавить ordering
    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f'{self.title}'
