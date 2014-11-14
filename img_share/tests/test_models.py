import unittest
from django.test import TestCase
from img_share.models import Image, User
from .factories import ImageFactory, UserFactory

class TestUserModel(TestCase):
  def test_create_user(self):
    instance = UserFactory.create()
    self.assertTrue(isinstance(instance, User))

class TestImageModel(TestCase):
  def test_create_image(self):
    instance = ImageFactory.create()
    self.assertTrue(isinstance(instance, Image))