from django.db import models

class User(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	password = models.CharField(max_length=50)

class Book(models.Model):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	isbn = models.CharField(max_length=13)
	publication_date = models.DateField()
