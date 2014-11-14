import unittest
from django.test import TestCase
from img_share.models import Image
from .factories import ImageFactory

class TestImageModel(TestCase):
  def test_create_image(self):
    assert ImageFactory.create()