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

description = """
    Toi, tu sais comment utiliser la console ! Jamais à court d'idées pour réaliser ton objectif, tu es déterminé-e et persévérant-e. Tes amis disent d'ailleurs volontiers que tu as du caractère et que tu ne te laisses pas marcher sur les pieds. Un peu hacker sur les bords, tu aimes trouver des solutions à tout problème. N'aurais-tu pas un petit problème d'autorité ? ;-)
    """
OpenGraphImage('Axel Arcidiaco', description)