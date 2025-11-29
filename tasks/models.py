from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    due_date = models.DateField()
    estimated_hours = models.IntegerField()
    importance = models.IntegerField()  # 1 se 10 ke beech
    dependencies = models.JSONField(default=list, blank=True)

def __str__(self):
    return self.title