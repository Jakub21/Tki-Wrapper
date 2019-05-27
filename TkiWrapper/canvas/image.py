import tkinter as tk
from PIL import Image as PImage
from PIL import ImageTk
import cv2
from TkiWrapper.canvas.point import Point

class Image:
    def __init__(self, path, anchor=(0, 0)):
        self.image = ImageTk.PhotoImage(file=path)
        self.anchor = Point(*anchor)
    def reInit(self, canvas):
        self.cnv = canvas
        self.anchorMode = canvas.ANCHOR_IMAGE
        self.stroke = canvas.STROKE_WIDTH
    def draw(self):
        anchor = self.anchor.transposedClone(self.cnv.ANCHOR, self.cnv.SCALE)
        if self.anchorMode == 'CENTER': anchorMode = tk.CENTER
        elif self.anchorMode == 'UPPERLEFT': anchorMode = tk.NW
        self.cnv.canvas.create_image(
            anchor.get(), image=self.image, anchor=anchorMode)

    @classmethod
    def fromPil(cls, image, anchor=(0, 0)):
        obj = cls.__new__(cls)
        obj.image = ImageTk.PhotoImage(image=image)
        obj.anchor = Point(*anchor)
        return obj

    @classmethod
    def fromCv2(cls, image, anchor=(0, 0)):
        obj = cls.__new__(cls)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        obj.image = ImageTk.PhotoImage(image=PImage.fromarray(image))
        obj.anchor = Point(*anchor)
        return obj
