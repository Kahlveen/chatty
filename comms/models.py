from django.db import models

class ChatMsg(models.Model):
	send_date = models.DateTimeField('date sent')
	msg = models.CharField(max_length=200)
	sender = models.CharField(max_length=200)
	recipient = models.CharField(max_length=200)
