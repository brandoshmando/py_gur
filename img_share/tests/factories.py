import factory
from pyfaker import Fake
from img_share.models import Image

fake = Fake(lang_code='en')

class ImageFactory(factory.Factory):
  FACTORY_FOR = Image

  title = "Test Title"
  artist_name = fake.Name.name()
  image_link = "http://examplelink.com"
