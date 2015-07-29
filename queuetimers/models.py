from django.db import models

# Create your models here.
class Timer(models.Model):
	queue = models.CharField(max_length=80)
	time = models.CharField(max_length=10)

	def __str__(self):
		return self.queue

	@property
	def shape_size(self):
		try:
			if int(self.time) in range(1,11):
				return int(self.time)
			else:
				return 11
		except:
			return 11