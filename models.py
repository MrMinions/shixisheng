from django.db import models

class Image(models.Model):
	img=models.ImageField(upload_to = './img')
class tImage(models.Model):
	name=models.CharField(max_length=30)
	data=models.CharField(max_length=350)
	img=models.ImageField(upload_to = './img')
class Text(models.Model):
	name = models.CharField(max_length=1024)
	text = models.CharField(max_length=1024)
class company(models.Model):
	name=models.CharField(max_length=64)
	intr=models.TextField()
	img=models.ImageField(upload_to = './img')