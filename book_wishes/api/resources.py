from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from api.models import *

class BookResource(ModelResource):
	class Meta:
		queryset = Book.objects.all()
		resource_name = 'book'
		authorization = Authorization()

class UserResource(ModelResource):
	class Meta:
		queryset = User.objects.all()
		resource_name = 'user'
		authorization = Authorization()
		# lock email and password
		excludes = ['email', 'password']
