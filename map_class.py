from pygame import image


class Map:
    def __init__(self, name):
        self.name = name
        self.char_map = []
        self.preview_img = image.load("maps/{}/map_preview.png".format(name))
