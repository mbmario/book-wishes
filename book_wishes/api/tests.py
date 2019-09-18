from django.test import TestCase

import datetime
from django.contrib.auth.models import User
from django.test import TestCase
from tastypie.test import ResourceTestCaseMixin
from api.models import *


class BookWishesTestCase(ResourceTestCaseMixin, TestCase):
	def setUp(self):
		super(BookWishesTestCase, self).setUp()
		self.book_url = '/api/v1/book/'
		self.user_url = '/api/v1/user/'

		self.new_book = {
			"title": "Persian Fire",
			"author": "Tom Holland",
			"ISBN": "123456",
			"publication_date": "01-01-2005"
		}

		self.new_user = {
			"first_name" : "Alice",
			"last_name" : "Example",
			"email" : "alice@example.com",
			"password" : "logon"
		}

	def test_get_detail_json(self):
		book_resp = self.api_client.get(self.book_url, format='json')
		user_resp = self.api_client.get(self.user_url, format='json')
		self.assertValidJSONResponse(book_resp)
		self.assertValidJSONResponse(user_resp)

	def test_post_user(self):
		self.assertHttpCreated(self.api_client.post('/api/v1/user/', format='json', data=self.new_user))

	def test_post_book(self):
		self.assertHttpCreated(self.api_client.post('/api/v1/book/', format='json', data=self.new_book))
