# Importation des bibliothèques Python
import random
import os
from fbapp.models import Content, Gender
from PIL import Image, ImageFont, ImageDraw
import textwrap


def find_content(gender):
    contents = Content.query.filter(Content.gender == Gender[gender]).all()
    return random.choice(contents)


class OpenGraphImage:

    def __init__(self, first_name, description):
        background = self.base()
        background.show()
        # textwrap découpe une chaine de caractères
        # sans couper les mots au milieu.
        sentences = textwrap.wrap(description, width=60)

        # current_h : Hauteur à laquelle commencer à écrire .
        # pad : pixels à ajouter entre chaque ligne, en hauteur.
        current_h, pad = 180, 10

        for sentence in sentences:
            w, h = self.print_on_img(background, sentence, 40, current_h)

            # on incrémente la hauteur pour créer une nouvelle ligne
            # en-dessous.
            current_h += h + pad

        background.show()

    def base(self):
        img = Image.new('RGB', (1200, 630), '#18BC9C')
        return img

    def print_on_img(self, img, text, size, height):
        # On commence par charger la police utilisée.
        font = ImageFont.truetype(os.path.join(
            'fbapp', 'static', 'fonts', 'Arcon-Regular.otf'), size)

        # Création d'une nouvelle instance
        draw = ImageDraw.Draw(img)

        # textsize renvoie la largeur et la hauteur en pixel
        # d'une chaine de caractères donnée.
        w, h = draw.textsize(text, font)

        # Calcul de la position pour que le texte soit centré
        # et non pas aligné à gauche.
        position = ((img.width - w) / 2, height)

        # Ajout du texte à l'image.
        draw.text(position, text, (255, 255, 255), font=font)
        
        # Nous devons renvoyer la largeur et la hauteur
        # pour imprimer le texte.
        return (w, h)


description = """
    Toi, tu sais comment utiliser la console ! Jamais à court d'idées pour réaliser ton objectif, tu es déterminé-e et persévérant-e. Tes amis disent d'ailleurs volontiers que tu as du caractère et que tu ne te laisses pas marcher sur les pieds. Un peu hacker sur les bords, tu aimes trouver des solutions à tout problème. N'aurais-tu pas un petit problème d'autorité ? ;-)
    """
OpenGraphImage('Axel Arcidiaco', description)
