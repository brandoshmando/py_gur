import unittest
from django.test import TestCase
from img_share.models import Image
from img_share.tests import factories

class TestImageModel(TestCase):
  def test_create_image():
    assert ImageFactroy.create()