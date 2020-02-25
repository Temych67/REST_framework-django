from django.db import models

class Chat(models.Model):
	email 					= models.EmailField(null=False,verbose_name="email", max_length=70)
	message 				= models.TextField(max_length=100, null=False)
	date_published 			= models.DateTimeField(auto_now_add=True, verbose_name="date published")
	date_updated 			= models.DateTimeField(auto_now=True, verbose_name="date updated")

	def __str__(self):
		return self.email