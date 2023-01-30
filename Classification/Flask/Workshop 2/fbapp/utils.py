import random
from fbapp.models import Content, Gender
from PIL import Image


def find_content(gender):
    contents = Content.query.filter(Content.gender == Gender[gender]).all()
    return random.choice(contents)


class OpenGraphImage:

    def __init__(self, first_name, description):
      background = self.base()
      background.show()

    def base(self):
      img = Image.new('RGB', (1200, 630), '#18BC9C')
      return img
