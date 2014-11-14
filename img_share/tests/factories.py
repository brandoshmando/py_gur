import factory
from pyfaker import Fake
from img_share.models import Image, User

fake = Fake(lang_code='en')

class UserFactory(factory.Factory):
  FACTORY_FOR = User

  first_name = "John"
  last_name = "Doe"
  email = "jon.d@example.com"
  password = "BlahBlah"

class ImageFactory(factory.Factory):
  FACTORY_FOR = Image

  title = "Test Title"
  artist_name = fake.Name.name()
  image_link = "http://examplelink.com"

