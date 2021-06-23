from django.db import models

# Create your models here.

class Project(models.Model):
	title=models.CharField(max_length=200)
	thumbnail=models.ImageField(upload_to='Projects/')
	body=models.TextField()
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

class Contact(models.Model):
	name=models.CharField(max_length=200)
	email=models.EmailField(max_length=200)
	message=models.TextField()
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name + ' ' + self.email