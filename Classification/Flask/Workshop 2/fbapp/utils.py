import random

from fbapp.models import Content, Gender


def find_content(gender):
    contents = Content.query.filter(Content.gender == Gender[gender]).all()
    return random.choice(contents)


class OpenGraphImage:

    def __init__(self, first_name, description):
        self.base()

    def base(self):
        # create a basic image
        pass
