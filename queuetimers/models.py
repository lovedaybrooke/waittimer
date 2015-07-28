from django.db import models

# Create your models here.
class Timer(models.Model):
	queue = models.CharField(max_length=80)
	time = models.CharField(max_length=10)

	def __str__(self):
		return self.queue